============
Installation
============


Requirements
------------
* `Python <https://www.python.org/>`_ (2.7, 3.\*)
* `Django <https://www.djangoproject.com/>`_ (1.11, 2.\*, 3.\*)


Installation
------------

Installing using `pip <https://pip.pypa.io/en/stable/quickstart/>`_::

    pip install django-adminlte2-templates



Add ``adminlte2_templates`` to ``INSTALLED_APPS``:

.. code:: python

    INSTALLED_APPS = [
        ...
        'adminlte2_templates',
    ]


Add ``adminlte2_templates.context_processors.template`` to ``context_processors``:

.. code:: python

    TEMPLATES = [
            ...
            'OPTIONS': {
                'context_processors': [
                    ...
                    'adminlte2_templates.context_processors.template',
                ],
            ...
    ]


Static files
------------

This module provides static files for the following client-side libraries out-of-the-box:

- AdminLTE 2.4.18 (``static/adminlte2/adminlte-2.4.18``)
- Bootstrap 3.4.1 (``static/adminlte2/bootstrap-3.4.1``)
- DataTables 1.10.21 (``static/adminlte2/datatables-1.10.21``)
- Font Awesome 4.7.0 (``static/adminlte2/fontawesome-4.7.0``)
- HTML5Shiv 3.7.3 (``static/adminlte2/html5shiv-3.7.3``)
- jQuery 3.5.1 (``static/adminlte2/jquery-3.5.1``)
- Respond.js 1.4.2 (``static/adminlte2/respond-1.4.2``)
- Select2 4.0.13 (``static/adminlte2/select2-4.0.13``)
