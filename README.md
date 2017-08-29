# Blog
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/Afonasev/Blog/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/Afonasev/Blog.svg?branch=master)](https://travis-ci.org/Afonasev/Blog)
[![Coverage Status](https://coveralls.io/repos/github/Afonasev/Blog/badge.svg?branch=master)](https://coveralls.io/github/Afonasev/Blog?branch=master)

### Installing deps

    pip install -r requirements.txt

### Migrations applying
    python manage.py migrate

### Running debug server

    python manage.py runserver

### Running the testsuite

    py.test --cov=./backend

### Code linting

    flake8 backend
    pylint backend

### Sort imports

    isort -rc backend

### Code Style

* [PEP8](https://www.python.org/dev/peps/pep-0008/)

### Git pre-commit hook

    #!/bin/bash
    set -e
    isort -c
    flake8 backend
    pylint backend
    py.test --cov=./backend
