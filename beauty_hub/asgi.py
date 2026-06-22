"""
ASGI config for beauty_hub project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os
from decouple import config

from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beauty_hub.settings')
mode = config('MODE')
if mode == 'production':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beauty_hub.settings.production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beauty_hub.settings.development')

application = get_asgi_application()
