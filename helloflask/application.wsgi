import os, sys

PROJECT_DIR = '/www/apps.crunch-tech.com/helloflask'

activate_this = os.path.joi(PROJECT_DIR, 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
sys.path.append(PROJECT_DIR)

from helloflask import app as application

