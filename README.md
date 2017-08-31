# Blog
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/Afonasev/Blog/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/Afonasev/Blog.svg?branch=master)](https://travis-ci.org/Afonasev/Blog)
[![Coverage Status](https://coveralls.io/repos/github/Afonasev/Blog/badge.svg?branch=master)](https://coveralls.io/github/Afonasev/Blog?branch=master)

### Run dev server

##### Install deps

    pip install -r requirements.txt

##### Apply migrations
    python manage.py migrate

##### Run debug server

    python manage.py runserver

### Tests, linters, etc.

##### Run all tests and linters

    ./scripts/test.sh

##### Run tests

    py.test --cov=./backend

##### Run linters

    flake8 backend
    pylint backend

##### Sort imports

    isort -rc backend

### Git pre-commit hook

    #!/bin/bash
    set -e
    isort -c
    flake8 backend
    pylint backend
    py.test --cov=./backend

### Code Style

* [PEP8](https://www.python.org/dev/peps/pep-0008/)
