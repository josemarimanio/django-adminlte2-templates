import io

from setuptools import find_packages
from setuptools import setup

from adminlte2_templates import __version__

with io.open('README.rst', 'rt', encoding='utf8') as f:
    README = f.read()

setup(
    name='django-adminlte2-templates',
    version=__version__,
    description='AdminLTE 2 templates for Django',
    long_description=README,
    url='https://github.com/josemarimanio/django-adminlte2-templates/',
    project_urls={
        'Documentation': 'https://django-adminlte2-templates.readthedocs.io/en/latest/',
        'Source Code': 'https://github.com/josemarimanio/django-adminlte2-templates/',
    },
    author='Jose Mari Manio',
    author_email='josemari.manio@outlook.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=2.7',
    install_requires=['django>=1.11', ],
)
