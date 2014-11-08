from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from filebrowser.sites import site

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^uvodna/', 'landing.views.landing_page'),
    url(r'', include('myflatpages.urls', namespace='myflatpages', app_name='myflatpages')),
    url(r'^kontakt/', include('contact.urls', namespace='contact', app_name='contact')),
    url(r'^dogadanja/', include('events.urls', namespace='events', app_name='events')),
    url(r'^slikovnice/', include('books.urls', namespace='books', app_name='books')),
    url(r'^galerija/', include('gallery.urls', namespace='gallery', app_name='gallery')),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    # url(r'^photologue/', include('photologue.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

# staticfiles_urlpatterns() returns only if DEBUG, static also
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
