# -*- coding: utf-8 -*-
from django.conf import settings

# 1048576 = 1mb
IMG_MAX_SIZE = getattr(settings, 'GALLERY_IMG_MAX_SIZE', 1048576 * 2)
# allowed content_type without 'image/' part
IMG_TYPES = getattr(settings, 'GALLERY_IMG_TYPES', ['jpeg'])
