# Load defaults in order to then add/override with dev-only settings
from base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
# Default : the opposite of DEBUG
COMPRESS_ENABLED = False

# Debug Toolbar
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
INTERNAL_IPS = ('127.0.0.1',)
INSTALLED_APPS += (
    'debug_toolbar',
)
DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}

# Verbose show warning
# http://docs.python.org/2/library/warnings.html#warnings.showwarning
import warnings
import traceback
def custom_showwarning(message, category, filename, lineno, **kwargs):
    warnings.formatwarning(message, category, filename, lineno)
    # traceback.print_exc()
warnings.showwarning = custom_showwarning
