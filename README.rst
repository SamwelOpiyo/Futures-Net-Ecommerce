Futures Net Ecommerce
=====================

Ecommerce API Interview Challenge.

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:License: MIT


Running Locally with Docker
---------------------------


See detailed `cookiecutter-django Running Locally with Docker documentation`_

.. _cookiecutter-django Running Locally with Docker documentation: https://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html


Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command:

::

    $ docker-compose -f local.yml run --rm django python manage.py createsuperuser

* The first time you login with the superuser account after its creation, you'll see a "Verify Your E-mail Address" page. Use the simulated email verification message from the console to activate the account.


Test coverage
^^^^^^^^^^^^^

To run the tests::

    $ docker-compose -f local.yml run --rm django coverage run -m pytest

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ docker-compose -f local.yml run --rm django pytest


API Docs
--------

After the docker environment is ready to access the docs, navigate to:

`API documentation http://127.0.0.1:8000/api/schema/ <http://127.0.0.1:8000/api/schema/>`_

* Every one including Anonymous Users can view data through the API.

* Only the Administrators/SuperUsers can create and edit information through the API.

* Therefore to be able to access all the endpoints of the API, you need to be authenticated as a superuser.


Guideline - Creating a Product
------------------------------

After the docker environment is ready to access the docs, navigate to:

`Product Creation Guidelines <docs/product_creation.rst>`_


Deployment
----------

The following details how to deploy this application.


Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html
