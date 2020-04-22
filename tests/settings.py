import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '!t_(11ght0&nmb&$tf4to=gdg&u$!hsm3@)c6dzp=zdc*c9zci'

INSTALLED_APPS = [
    'django.contrib.sites',

    'adminlte2_templates',

    'tests',
]

ROOT_URLCONF = 'tests.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'tests/templates')],
        'OPTIONS': {
            'context_processors': [
                'adminlte2_templates.context_processors.template',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
