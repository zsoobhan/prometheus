import datetime

from fabric.decorators import runs_once
from fabric.operations import put, prompt
from fabric.colors import green, white, _wrap_with, red, cyan, magenta, yellow
from fabric.api import local, cd, sudo
from fabric.contrib.files import exists

from fabconfig import env

# def deploy should do the following:
# get branch
# fetch origin master
# merge master locally
# push to origin
# create the gir archive
# push the archive
# unzip the archive on the machine
# create the virtualenv
# static files
# deploy nginx
# restart nginx
# reload supervisor
# empty /tmo/

def notify(msg, col=green, wrap='0'):
    bar = '+-%s-+' % '-'*len(msg)
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


def _set_branch_information():
    env.last_commit = local('git rev-parse HEAD', capture=True)
    env.branch = local('git symbolic-ref --short HEAD', capture=True)
    env.build_name = '%s%s' % (
        env.branch, datetime.datetime.now().strftime('%Y-%m-%d-%H-%M'))
    env.build_path = '/tmp/build-%(build_name)s.tar.gz' % env
    env.code_dir = '%s/%s' % (env.builds_dir, env.build_dir)


@runs_once
def do_git_stuff():
    notify('updating branch %(branch)' % env)
    local('git pull origin %(branch)s' % env)
    local('git push origin %(branch)s' % env)


def create_and_push_archive():
    notify('Zipping up and putting archive on server')
    _set_branch_information()
    local('''git archive --format tar %(branch)s %(web_dir)s
             | gzip > %(build_path)s ''' % env)
    put(env.build_path, env.build_path)


def provision_server():
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
        ]

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
        sudo('mkdir -p %(virtualenv_dir)s' % env)
        with cd(env.virtualenv):
            [sudo(cmd) for cmd in v_env_commands]


def make_folder_structure():
    sudo('mkdir -p %(builds_dir)s' % env)
    cmds = [
        'mkdir -p builds/%(builds_name)s',
        'mkdir -p data/%(build)s',
        'mkdir -p logs/%(build)s',
        'mkdir -p media/%(build)s',
        'mkdir -p run/%(build)s',
        'chmod -R g+w logs/ media/ run/',
        '''
           chown -R %(webserver_user)s:%(webserver_user) -R
           data/ logs/ media/ run/
        ''',
    ]
    with cd(env.project_dir):
        [sudo(cmd % env) for cmd in cmds]


def unpack():
    # make folder structure
    sudo('mkdir -p %(builds_dir)s' % env)
    with cd(env.builds_dir):
        sudo('mkdir %(build_name)s')
        sudo('tar -xzf %(build_path)s -C %(build_name)' % env)


def upload_confs():
    'uploading nginx and supervisor confs'
    confs = [('%(nginx_conf)s' % env, '/etc/nginx/sites-enabled/'),
             ('%(supervisor_conf)s' % env, 'etc/supervisor/conf.d/'),
             ('deploy/requirements.txt', '/tmp/'), ]
    [put(c[0], c[1]) for c in confs]


def touch_reload_wsgi():
    notify('Reloading python code.')
    with cd(env.builds_dir):
        sudo('touch %(build)s/%(wsgi)s' % env)


def set_permissions():
    notify("Applying permissions")
    with cd(env.code_dir):
        sudo('chmod -R 775 public')
        sudo('chown -R root:%(webserver_user)s public' % env)

# TODO:
# collect_static, migrate, clean-up (/tmp/), switch symlink
# reload supervisor
# reload nginx


def _activate_virtualenv():
    return 'source %(virtualenv)sbin/activate && ' % env


def update_virtualenv():
    sudo(_activate_virtualenv+'pip install -r tmp/requirements.txt' % env)






