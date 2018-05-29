# -*- coding: utf-8 -*-
"""
WSGI config for InventoryMaster project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "InventoryMaster.settings")

#使用dj_static將會從static_url來的訪問導至static_root中抓取靜態檔案
application = Cling(get_wsgi_application())
