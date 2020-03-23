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
