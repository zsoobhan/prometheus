==================================
Prometheus - http://zsoobhan.co.uk
==================================

Introduction
------------
Ziyad Soobhan's personal website/project.
This a Django 1.7.x with a fabric deploy script. It is designed to be 
repeatable and painless to set up again if the infrastructure changes i.e.
when I run out of the AWS Free Tier offer. 

The content served is split between a few flat TemplateViews and a rudimentary
CMS built primarily with the django Admin Site with some extra eye-candy such as
CKEditor. The static files are served using Amazon S3 to take the load of the 
tiny server it is deployed to. There is also a contact form which saves content
to the database as well as sends an email using an post_save.connect signal. 
There is also some basic context processing/middleware here and there which
generates a dynamic/semi random question to be saved in the session which is then
used in form processing to verify if the user is a robot. 

The majority of the project has been built in my spare time in 15-30 minute 
chunks while on the tube and development is ongoing.




Analytics
---------

The project uses Universal Analytics from Google to track basic page views
as well as certain button clicks. I plan on using more of the Google Tag Manager
features as and when required after the implementation of the blog.


Infrastructure
--------------
This project has been set up to run on the AWS Free Tier infrastructure.
It uses a PostGres database backend stored on an RDS instance and uses 
SES to send email alerts. The static files are served by S3 with the exception
of the robots.txt and favicon.ico which are more served directly by nginx. 


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
  - .sh



Status
------
Up and running with limited content and working CMS-driven blog. 


Acknowledgements
----------------
The overall structure has been inspired by tangentlabs/tangent-django-boilerplate.

The design was inspired by templated.co/plushiness which has been modified to
be more responsive. 

