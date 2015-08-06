#!/usr/bin/env bash

virtualenv pkgenv
pkgenv/bin/pip install -r reqs_pip.txt
pkgenv/bin/pip install -r pkg_reqs_pip.txt
pkgenv/bin/python setup.py bdist_wheel
