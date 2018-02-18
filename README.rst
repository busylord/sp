Django Coleman
==============

Task Management webapp 
with **Django Admin** and modified version of Coleman.


Features
--------

* A simple task management web app for teams.

.. image:: docs/source/_static/img/Screenshot%20(24).png
   :alt: Django Success Plus


Requirements
------------

* Python 3.4+ (tested with Python 3.4 and 3.6).
* Django 2.0 and other dependencies declared
  in the ``requirements.txt`` file (use virtual environments!).
* A Django compatible database like PostgreSQL (by default uses
  the Python's built-in SQLite database for development purpose).





Available settings to override are:

* ``DEBUG``: set the Django ``DEBUG`` option. Default ``True``.
* ``TIME_ZONE``: default ``UTC``. Other example: ``America/Buenos_Aires``.
* ``LANGUAGE_CODE``: default ``en-us``. Other example: ``es-ar``.
* ``SITE_HEADER``: Header title of the app. Default to *"Django Coleman - A Simple Task Manager"*.
* ``DATABASE_URL``: Database string connection. Default uses SQLite database. Other
  example: ``postgresql://dcoleman:postgres@localhost/dcoleman_dev``.

To run in a production environment, check the `<README-production.rst>`_ notes, or
see the official Django documentation.


Access the application
----------------------

Like any Django app developed with Django Admin, enter with: http://localhost:8000


Development
-----------

Some tips if you are improving this application.

Translations
^^^^^^^^^^^^

After add to the source code new texts to be translated, execute
from the root folder (replace ``LANG`` by a valid language
code like ``es``)::

    $ django-admin makemessages -l LANG

Then go to the *.po* file and add the translations. Finally
execute to compile the locales::

    $ django-admin compilemessages



About
-----

**Project**: https://github.com/mayankshekhar03/furry-happiness

**Authors**: (2017-2018) Mayank Shekhar <mayankshekhar03@gmail.com> with special thanks to Mariano Ruiz <mrsarm@gmail.com>

**License**: AGPL-v3
