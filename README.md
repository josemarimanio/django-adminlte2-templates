AdminLTE 2 templates for Django
===============================

**django-adminlte2-templates** provide templates to easily integrate [AdminLTE 2](https://adminlte.io/) to your Django projects.

For more information, please see the [documentation](https://django-adminlte2-templates.readthedocs.io/en/latest/) online. 
Alternatively, the documentation is also available in the `docs` directory of the project. 


Requirements
------------
- Python (2.7, 3.\*)
- Django (1.11, 2.\*, 3.\*)


Installation
------------

Installing using [pip](https://pip.pypa.io/en/stable/quickstart/):
```
pip install django-adminlte2-templates
```

Add `adminlte2_templates` to `INSTALLED_APPS`:
```
INSTALLED_APPS = [
    ...
    'adminlte2_templates',
]
```

Add `adminlte2_templates.context_processors.template` to `context_processors`:
```
TEMPLATES = [
        ...
        'OPTIONS': {
            'context_processors': [
                ...
                'adminlte2_templates.context_processors.template',
            ],
        ...
]
```


Links
-----

- Documentation: [https://django-adminlte2-templates.readthedocs.io/en/latest/](https://django-adminlte2-templates.readthedocs.io/en/latest/)
- GitHub: [https://github.com/josemarimanio/django-adminlte2-templates/](https://github.com/josemarimanio/django-adminlte2-templates/)
- PyPi: [https://pypi.org/project/django-adminlte2-templates/](https://pypi.org/project/django-adminlte2-templates/)
