#!/usr/bin/env bash
rm -rf build/
rm -rf dist/
rm -rf django_adminlte2_templates.egg-info/
python setup.py sdist bdist_wheel
