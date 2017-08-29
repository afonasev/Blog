import os

PROJECT = 'BLOG'
PRODUCTION = os.environ.get('PRODUCTION', False)
DEBUG = not PRODUCTION
