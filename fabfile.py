import datetime

from fabric.decorators import runs_once
from fabric.operations import put, prompt
from fabric.api import local, cd, sudo
from fabric.contrib.files import exists
from fabric.colors import green, _wrap_with, red, cyan, magenta

from fabconfig import env, prod


def deploy():
    set_branch_information()
    do_git_stuff()
    set_ssh_user()
    provision_server()
    make_folder_structure()
    make_virtualenv()
    create_and_push_archive()
    unpack()
    move_confs()
    upload_settings()
    update_virtualenv()
    manage_new_code()
    switch_symlink()
    set_permissions()
    touch_reload_wsgi()
    restart_nginx()
    restart_supervisor()
    clean_tmp_dir()


def notify(msg, col=green, wrap='0'):
    bar = '+-%s-+' % ('-'*len(msg))
    print ''
    print col(bar)
    print _wrap_with(wrap)(col("| %s |" % msg))
    print col(bar)
    print ''


def set_ssh_user():
    user = prompt(
        red('User for remote host? Defaults to %(remote_user)s' % env))
    if user:
        env.user = user
    else:
        env.user = env.remote_user


def set_branch_information():
    env.last_commit = local('git rev-parse HEAD', capture=True)
    env.raw_branch_name = local('git symbolic-ref --short HEAD', capture=True)
    env.branch = env.raw_branch_name.replace('/', '_')
    env.build_name = '%s%s' % (
        env.branch, datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
    env.build_path = '/tmp/build-%(build_name)s.tar.gz' % env
    env.code_dir = '%(project_dir)s/builds/%(build_name)s/' % env


@runs_once
def do_git_stuff():
    'updates local branch and pushes it.'
    sync = prompt(magenta('Sync with repo? [Y/n]'))
    if sync.strip() not in ['n', 'N']:
        notify('Syncing with git repo', col=cyan)
        notify('updating branch %(raw_branch_name)s' % env)
        local('git pull origin %(raw_branch_name)s' % env)
        local('git push origin %(raw_branch_name)s' % env)


def create_and_push_archive():
    notify('Zipping up and putting archive on server')
    local('git archive --format tar %(raw_branch_name)s %(web_dir)s | gzip > %(build_path)s ' % env)  # noqa
    put(env.build_path, env.build_path)


def provision_server():
    notify('Provisioning Server!')
    apt_get_cmds = [
        'update -qq',
        'install -y build-essential',
        'install -y libpq-dev',
        'install -y libxml2-dev',
        'install -y libxslt1-dev',
        'install -y libgeoip-dev',
        'install -y libgeos-dev',
        'install -y libjpeg-dev',
        'install -y python-dev',
        'install -y python-pip',
        'install -y supervisor',
        'install -y uwsgi',
        'install -y libproj-dev',
        'install -y memcached',
        'install -y nginx',
        'install -y postgresql',
        'install -y postgresql-contrib',
        ]
    provision = prompt(red('Provision Server? [y/N]'))
    if provision.strip() in ['y', 'Y']:
        for cmd in apt_get_cmds:
            sudo('apt-get %s' % cmd)
        sudo('apt-get clean &&  apt-get autoclean')
        sudo('pip install virtualenv')


def make_virtualenv():
    v_env_commands = [
        '`which virtualenv` --no-site-packages . ',
        'echo "export DJANGO_CONF=\"conf.%(build)s\"" >> /bin/activate' % env,
    ]

    if not exists(env.virtualenv):
        notify('Making VirtualEnv')
        sudo('mkdir -p %(virtualenv)s' % env)
        with cd(env.virtualenv):
            [sudo(cmd) for cmd in v_env_commands]


def make_folder_structure():
    notify('Making folder structure.')
    sudo('mkdir -p %(builds_dir)s' % env)
    cmds = [
        'mkdir -p builds/%(build_name)s',
        'mkdir -p data/%(build)s',
        'mkdir -p logs/%(build)s',
        'mkdir -p media/%(build)s',
        'mkdir -p run/%(build)s',
        'chmod -R g+w logs/ media/ run/',
        'chown -R %(webserver_user)s:%(webserver_user)s data/ ',
        'chown -R %(webserver_user)s:%(webserver_user)s media/',
        'chown -R %(webserver_user)s:%(webserver_user)s logs/ ',
        'chown -R %(webserver_user)s:%(webserver_user)s run/',
    ]
    with cd(env.project_dir):
        [sudo(cmd % env) for cmd in cmds]


def unpack():
    notify('Unpacking codebase')
    sudo('mkdir -p %(builds_dir)s' % env)
    with cd(env.builds_dir):
        sudo('if [ -d "%(build_name)s" ]; then rm -rf "%(build_name)s"; fi' % env)  # noqa
        sudo('mkdir %(build_name)s' % env)
        sudo('tar -xzf %(build_path)s -C %(build_name)s' % env)
    with cd(env.code_dir):
        sudo('mv www/* . && rm -rf www')


def move_confs():
    notify('Copyting Nginx, Supervisor and Logrotate confs to their '
           'respective destinations')
    cmds = [
        'cp deploy/nginx/%(build)s.conf /etc/nginx/sites-enabled/%(project_code)s%(build)s.conf',  # noqa
        'cp deploy/supervisord/%(build)s.conf /etc/supervisor/conf.d/%(project_code)s%(build)s.conf',  # noqa
        'cp deploy/logrotate.d/application /etc/logrotate.d/app.%(project_code)s%(build)s',  # noqa

    ]
    with cd(env.code_dir):
        [sudo(cmd % env) for cmd in cmds]


def touch_reload_wsgi():
    notify('Reloading python code.')
    with cd(env.builds_dir):
        sudo('touch %(build)s/%(wsgi)s' % env)


def set_permissions():
    notify("Applying permissions")
    with cd(env.code_dir):
        sudo('chmod -R 775 public')
        sudo('chown -R root:%(webserver_user)s public' % env)

    with cd(env.project_dir):
        sudo('chown -R www-data:www-data run/ logs/ builds/ media/')


def _activate_virtualenv():
    return 'source %(virtualenv)sbin/activate && ' % env


def update_virtualenv():
    notify('Updating VirtualEnv')
    with cd(env.code_dir+'/deploy'):
        sudo(_activate_virtualenv() + 'pip install -r requirements.txt')


def manage_new_code():
    'Updates database and deals with static files'
    notify('Migrate and collecstatic are about to happen...')
    cmds = [
        './manage.py migrate',
        './manage.py collectstatic --noinput']

    for cmd in cmds:
        with cd(env.code_dir):
            sudo(_activate_virtualenv() + cmd)


def upload_settings():
    notify('Uploading non-version controlled settings %(build)s.py' % env)
    put('www/conf/%(build)s.py' % env, '/tmp/')
    sudo('mv /tmp/%(build)s.py %(code_dir)s/conf/' % env)


def restart_nginx():
    notify('Re-starting Nginx')
    sudo('service nginx restart')


def restart_supervisor():
    notify('Restarting App from supervisorctl')
    sudo('supervisorctl restart %(client)s-%(project_code)s-%(build)s' % env)


def clean_tmp_dir():
    notify('Clean up on aisle 3!')
    cmd = 'rm -rf %(build_path)s' % env
    sudo(cmd)
    local(cmd)


def switch_symlink():
    notify("Switching symlinks")
    with cd(env.builds_dir):
        sudo('if [ -h %(build)s ]; then unlink %(build)s; fi' % env)
        sudo('ln -s %(code_dir)s %(build)s' % env)
