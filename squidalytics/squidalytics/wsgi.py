"""
WSGI config for squidalytics project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

import dotenv
from django.core.wsgi import get_wsgi_application

project_folder = os.path.expanduser("~/squidalytics")
dotenv.load_dotenv(os.path.join(project_folder, ".env"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "squidalytics.settings")

application = get_wsgi_application()
