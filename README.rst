Octopod Spork 🐙
================

Please sign the petition_ for a spork emoji 

.. _petition: https://www.change.org/p/apple-we-as-a-union-ad-people-need-a-spork-emoji-now


.. image:: https://img.shields.io/github/workflow/status/pydanny/cookiecutter-django/CI/master
    :target: https://github.com/pydanny/cookiecutter-django/actions?query=workflow%3ACI
    :alt: Build Status

.. image:: https://www.codetriage.com/pydanny/cookiecutter-django/badges/users.svg
    :target: https://www.codetriage.com/pydanny/cookiecutter-django
    :alt: Code Helpers Badge

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black
    :alt: Code style: black

Powered by Cookiecutter, Octopod Spork is a framework for jumpstarting production-ready Django projects quickly.


Overview
---------
Octopod Spork is a spin off of Cookiecutter Django. It is customized for my workflow and includes features such as PostGIS, Selenium, Celery volumes, REST authentication via API endpoints, Bash scritps, etc.


Usage
-----

First, get Cookiecutter. Trust me, it's awesome::

    $ pip install "cookiecutter>=1.7.0"

Now run it against this repo::

    $ cookiecutter https://github.com/julianwagle/octopod-spork

You'll be prompted for some values. Provide them, then a project will be created for you.

Finally, move to the root directory and enter the following::

    $ docker-compose -f local.yml up
    

Troubleshooting
---------------

IF you opt in to both Celery AND PostGIS, the first time you start this up, celerybeat may not properly insert a colomn into the database. However, the second time it will all work fine.

