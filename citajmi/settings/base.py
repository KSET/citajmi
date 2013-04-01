# Django settings for citajmi project.
import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(BASE_DIR, '../..'))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Andro Rezic', 'droan@kset.org'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'sqlite.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Europe/Zagreb'
# LANGUAGE_CODE = 'en-US'
LANGUAGE_CODE = 'hr-HR'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

PREPEND_WWW = False

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'landing.middlewares.LandingPageMiddleware',
)

# Enable request context variable in flatpages
TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
    'events.context_processors.current_events',
)

ROOT_URLCONF = 'citajmi.urls'
WSGI_APPLICATION = 'citajmi.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.admindocs',
    'django.contrib.flatpages',
    'grappelli.dashboard',
    'grappelli',
    'filebrowser',
    'bootstrapform',
    'tinymce',
    'photologue',
    'south',
    'tagging',
    'compressor',
    'django.contrib.admin',

    'citajmi',
    'myflatpages',
    'contact',
    'events',
    'books',
    'gallery',
    'landing',
    'django_cleanup',
)


GRAPPELLI_ADMIN_TITLE = 'Citajmi.info'
GRAPPELLI_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'

# Main FileBrowser Directory 'uploads/'. Leave empty in order to browse all from MEDIA_ROOT
FILEBROWSER_DIRECTORY = 'uploads/'
FILEBROWSER_DIRECTORY = ''
FILEBROWSER_DEFAULT_SORTING_BY = 'filename_lower'

FILEBROWSER_VERSIONS = {
    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
    'thumbnail': {'verbose_name': 'Thumbnail (60px)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'small': {'verbose_name': 'Small (140px)', 'width': 140, 'height': '', 'opts': ''},
    'medium': {'verbose_name': 'Medium (300px)', 'width': 300, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Big (460px)', 'width': 460, 'height': '', 'opts': ''},
    'large': {'verbose_name': 'Large (680px)', 'width': 680, 'height': '', 'opts': ''},
}
# Versions available within the Admin-Interface.
FILEBROWSER_ADMIN_VERSIONS = ['thumbnail', 'small', 'medium', 'big', 'large']
# Which Version should be used as Admin-thumbnail.
FILEBROWSER_ADMIN_THUMBNAIL = 'admin_thumbnail'


FILEBROWSER_SELECT_FORMATS = {
    'File': ['Folder','Document',],
    'Image': ['Folder','Image',],
    'Media': ['Video','Sound'],
    'Document': ['Document'],
    # for TinyMCE we can also define lower-case items
    'image': ['Image'],
    'file': ['Folder','Image','Document',],
}


# tinymce settings, add/remove buttons and so on
TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'theme_advanced_toolbar_location' : "top",
    'theme_advanced_resizing' : True,
    'plugins' : 'table,contextmenu,paste,autoresize,media,lists,style',
    # 'height' : 600,
    # 'width' : 800,
    'theme_advanced_buttons1': "formatselect,style,bold,italic,underline,separator,bullist,separator,outdent,indent,separator,undo,redo",
    'theme_advanced_buttons2': "cleanup,code,separator,lists,pasteword,table,contextmenu,media,style,image,link",
    # 'theme_advanced_buttons3': "",
}

import photologue
import time
from django.template.defaultfilters import slugify

def PHOTOLOGUE_PATH(instance, filename):
    typ = type(instance)
    from events.models import EventImg
    from books.models import BookImg
    from gallery.models import EntryImg
    # time.strftime('folder/%Y/%m/%d/')
    if typ is EventImg:
        folder = time.strftime('eventimgs/%Y/%m/')
        extension = os.path.splitext(filename.lower())[1]   # .jpg
        filename = '%s%s' % (slugify(instance.event.title), extension)
    elif typ is BookImg:
        folder = 'bookimgs/cat-%d/' % instance.book.category
        extension = os.path.splitext(filename.lower())[1]   # .jpg
        filename = '%s%s' % (slugify(instance.book.title), extension)
    elif typ is EntryImg:
        folder = time.strftime('galleryimgs/%Y/W/').replace('W', '%02d' % int(time.strftime('%W'))) # %W week in year 1-53
        extension = os.path.splitext(filename.lower())[1]   # .jpg
        filename = '%s-%d%s' % (slugify(instance.entry.full_name), instance.entry.id, extension)
    else:
        folder = 'photos'
    return os.path.join(photologue.models.PHOTOLOGUE_DIR, folder, filename)
