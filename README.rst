==================================
Prometheus - http://zsoobhan.co.uk
==================================

Introduction
------------
Ziyad Soobhan's personal website/project.
This a Django 1.7.x with a fabric deploy script. It is designed to be 
repeatable and painless to set up again if the infrastructure changes i.e.
when I run out of the AWS Free Tier offer. 

The content is mostly flat with a content served using the TemplateView.
There is also a contact form which saves content to the database as well as
sends an email using an post_save.connect signal. There is also some basic 
context processing and middleware which provides a dynamic question, saved in
the session, to the form. This is then used to verify if the user is a robot.

The majority of the project has been built in my spare time in 15-30 minute 
chunks while on the tube.


Future
------

The blog page is currently blank and will use a CMS. At the moment, I am looking
at Django CMS however this may change if I come across something more fit for
purpose.


Analytics
---------

The project uses Universal Analytics from Google to track basic page views
as tracking events on button clicks.
I plan on using more of the Google Tag Manager features as and when required
after the implementation of the blog.


Infrastructure
--------------
This project has been set up to run on the AWS Free Tier infrastructure.
It uses a PostGres database backend stored on an RDS instance and uses 
SES to send email alerts. 


VirtualEnv:

  - All libraries required for the project are installed in its own namepaced
    virtual environment.

Database:

  - PostgreSQL 9.3 on RDS instance

Server (T2 Micro):

  - Supervisor
  - WSGI
  - Nginx

App:

  - Django 1.7
  
Deploy:

  - Fabric



Status
------
Up and running with limited content.


Acknowledgements
----------------
The overall structure has been inspired by 
tangentlabs/tangent-django-boilerplate.

The design was inspired by templated.co/plushiness which has been modified to
be more responsive. 

