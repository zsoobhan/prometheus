==========
Prometheus
==========

Introduction
------------
Ziyad Soobhan's personal website/project.
Yes, it's over-complicated and over-engineered.
I don't need a namespaced virtual environment, nor a database for that matter.
I probably could have served the content entirely from Nginx and be done with it.
However the purpose of this site is for me to mess around a little bit with
various technologies. There is a docker branch too which runs locally. Most of
it has been built in 10-25 minute chunks of spare time and will be liable
to change when I make proper time for it.



TO DO
-----

  - The deploy script needs some work and re-factoring...but it works at least.
  - Add some content - About me page, contact me form, photography, climbing etc
  - Set up emails and reporting
  - Set up some proper analytics, tag manager etc
  

Infrastructure
--------------
Free tier AWS setup with RDS instance.

Name-spacing:

  - virtualenv (made sense at the time, not sure now)

Database:

  - PostgreSQL 9.3 on RDS instance

Server (t2 micro):

  - Supervisor
  - WSGI
  - Nginx

App:

  - Django 1.7
  
Deploy:

  - Fabric



Status
------
Deployed but without content.


Acknowledgements
----------------
The overall structure has been inspired by 
tangentlabs/tangent-django-boilerplate. 
