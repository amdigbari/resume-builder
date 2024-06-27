"""
ASGI config for _base project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import logging
import os

from django.core.asgi import get_asgi_application
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

logger = logging.getLogger(__name__)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "_base.settings")

application = get_asgi_application()
try:
    application = SentryAsgiMiddleware(application)
except Exception:
    logger.warning("Could'nt apply SentryAsgiMiddleware")
