from fabric.api import env

env.client = "zsoobhan"
env.project_code = "prometheus"

env.web_dir = "www"

# Environment-agnostic folders
env.project_dir = "/var/www/%(client)s/%(project_code)s" % env
env.static_dir = "/mnt/static/%(client)s/%(project_code)s" % env
env.builds_dir = "%(project_dir)s/builds" % env


def _configure(build_name):
    env.build = build_name
    env.virtualenv = "%(project_dir)s/virtualenvs/%(build)s/" % env
    env.data_dir = "%(project_dir)s/data/%(build)s/" % env
    env.nginx_conf = "www/deploy/nginx/%(build)s.conf" % env
    env.supervisord_conf = "www/deploy/supervisord/%(build)s.conf" % env
    env.wsgi = "deploy/wsgi/%(build)s.wsgi" % env
    env.webserver_user = "www-data"


def prod():
    _configure("prod")
    env.hosts = ["46.101.74.134"]
    env.remote_user = "root"


def test():
    _configure("test")
    env.remote_user = "ubuntu"
