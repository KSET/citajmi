#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

# populate db with custom photo sizes
def main():
    from photologue.models import PhotoSize
    sizes = (
        PhotoSize(name='gallery_display', width=1024, height=768),
        PhotoSize(name='gallery_thumbnail', width=300, height=225, upscale=True, crop=True),
        PhotoSize(name='event_thumbnail', width=300),
        PhotoSize(name='book_thumbnail', width=300, height=300),
    )
    counter = 0
    for size in sizes:
        if not PhotoSize.objects.filter(name=size.name).exists():
            size.save()
            print 'Created: %s' % size.name
            counter += 1
        else:
            print 'Not created: %s' % size.name
    print 'Created %d photo sizes.' % counter

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "citajmi.settings")
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    PROJECT_DIR = os.path.abspath(os.path.join(BASE_DIR, '..'))
    if PROJECT_DIR not in sys.path:
        sys.path.append(PROJECT_DIR)
    main()
