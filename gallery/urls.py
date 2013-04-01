from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('gallery.views',
    url(r'^$', 'album_list', name='album_list'),
    url(r'^(?P<year>\d{4})/$', 'album_archive', name='album_archive'),
    url(r'^album/(?P<album_id>\d+)/$', 'album_detail', name='album_detail'),
    url(r'^nagradna-igra/$', 'entry_add', name='entry_add'),
)
