import os
import sys

sys.path.append('/var/www/thecat/application')
sys.path.append('/var/www/thecat/settings')
os.environ['PYTHON_EGG_CACHE'] = 'var/www/thecat/.python-egg'
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.local'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
