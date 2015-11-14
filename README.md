==================================
Prometheus - http://zsoobhan.co.uk
==================================

[![Build Status](https://travis-ci.org/zsoobhan/prometheus.svg?branch=master)](https://travis-ci.org/zsoobhan/prometheus)

Introduction
------------
Ziyad Soobhan's personal website/project.
This a Django 1.7.x with a fabric deploy script. It is designed to be
repeatable and painless to set up again if the infrastructure changes



Analytics
---------
The project uses Universal Analytics from Google to track basic page views
as well as certain button clicks. I plan on using more of the Google Tag Manager
features as and when required after the implementation of the blog.


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

  - Django 1.7

Deploy:

  - Fabric
  - .sh



Status
------
Up and running with limited content and working CMS-driven blog... with no blog entries yet


Acknowledgements
----------------
The overall structure has been inspired by tangentlabs/tangent-django-boilerplate.

The design was inspired by templated.co/plushiness which has been modified to
be more responsive.  
