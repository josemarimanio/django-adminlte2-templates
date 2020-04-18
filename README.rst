
.. image:: https://img.shields.io/pypi/status/django-adminlte2-templates
    :target: https://pypi.org/project/django-adminlte2-templates

.. image:: https://img.shields.io/pypi/v/django-adminlte2-templates
    :target: https://pypi.org/project/django-adminlte2-templates

.. image:: https://readthedocs.org/projects/django-adminlte2-templates/badge/?version=latest
    :target: https://django-adminlte2-templates.readthedocs.io/en/latest

.. image:: https://img.shields.io/github/license/josemarimanio/django-adminlte2-templates
    :target: https://github.com/josemarimanio/django-adminlte2-templates/blob/master/LICENSE


AdminLTE 2 templates for Django
===============================

**django-adminlte2-templates** provides templates to easily integrate `AdminLTE 2 <https://adminlte.io/>`_ to your Django projects.

For more information, please see the `documentation <https://django-adminlte2-templates.readthedocs.io/en/latest/>`_ online.
Alternatively, the documentation is also available in the ``docs`` directory of the project.

This Django module assumes that you have prior experience with AdminLTE 2.
Please check the `AdminLTE 2 documentation <https://adminlte.io/docs/2.4/layout>`_ online for your reference.


Requirements
------------
- Python (2.7, 3.\*)
- Django (1.11, 2.\*, 3.\*)


Installation
------------

Installing using `pip <https://pip.pypa.io/en/stable/quickstart/>`_:

.. code-block:: console

    pip install django-adminlte2-templates


Add ``adminlte2_templates`` to ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'adminlte2_templates',
    ]


Add ``adminlte2_templates.context_processors.template`` to ``context_processors``:

.. code-block:: python

    TEMPLATES = [
            ...
            'OPTIONS': {
                'context_processors': [
                    ...
                    'adminlte2_templates.context_processors.template',
                ],
            ...
    ]



This module provides static files for the following client-side libraries out-of-the-box:

- AdminLTE 2.4.18 (``static/adminlte2/adminlte-2.4.18``)
- Bootstrap 3.4.1 (``static/adminlte2/bootstrap-3.4.1``)
- Font Awesome 4.7.0 (``static/adminlte2/fontawesome-4.7.0``)
- HTML5Shiv 3.7.3 (``static/adminlte2/html5shiv-3.7.3``)
- jQuery 3.4.1 (``static/adminlte2/jquery-3.4.1``)
- Respond.js 1.4.2 (``static/adminlte2/respond-1.4.2``)


Quickstart
----------

Head to the `Quickstart <https://django-adminlte2-templates.readthedocs.io/en/latest/quickstart.html>`_ section of the documentation online for an example usage of **django-adminlte2-templates**.

Also, an example Django project ``example_project`` is included in the module for your reference.


Links
-----

- Documentation: `https://django-adminlte2-templates.readthedocs.io/en/latest/ <https://django-adminlte2-templates.readthedocs.io/en/latest/>`_
- Source Code: `https://github.com/josemarimanio/django-adminlte2-templates/ <https://github.com/josemarimanio/django-adminlte2-templates/>`_
- Package: `https://pypi.org/project/django-adminlte2-templates/ <https://pypi.org/project/django-adminlte2-templates/>`_
- AdminLTE 2: `https://adminlte.io/themes/AdminLTE/index2.html/ <https://adminlte.io/themes/AdminLTE/index2.html/>`_
