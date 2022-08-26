Prometheus - http://zsoobhan.co.uk
==================================

Deprecation Warning
-------------------

Everything here is decades old tech and needs to be replaced with a static website.

See `local_deploy_requirements.txt` for the python3 deployment requirements. Good luck.

[![Build Status](https://travis-ci.org/zsoobhan/prometheus.svg?branch=master)](https://travis-ci.org/zsoobhan/prometheus)

Modern(ish) Local Setup
-----------------------

```bash
cp www/conf/local.py.sample www/conf/local.py
cd docker
docker-compose run --service-ports website bash
./manage.py migrate
./manage.py runserver 0:8000
```

Introduction
------------
Ziyad Soobhan's personal website/project.
This a Django 1.8.x with a fabric deploy script. It is designed to be
repeatable and painless to set up again if the infrastructure changes


Infrastructure
--------------
VirtualEnv:

  - All libraries required for the project are installed in its own namepaced
    virtual environment.

Database:

  - PostgreSQL 9.3

Server Stack:

  - Supervisor
  - WSGI
  - Nginx
  - AWS S3 (static files)

App:

  - Django 1.8

Deploy:

  - Fabric
  - .sh


Acknowledgements
----------------
The overall structure has been inspired by tangentlabs/tangent-django-boilerplate.

The design was inspired by templated.co/plushiness which has been modified to
be more responsive.
