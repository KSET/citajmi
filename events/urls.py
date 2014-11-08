from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'events.views',
    url(r'^$', 'event_list', name='event_list'),
    url(r'^prijavi/$', 'event_add', name='event_add'),
    url(r'^opsirnije/(?P<slug>[\w-]+)/$', 'event_detail', name='event_detail'),
    url(r'^arhiva/(?P<year>\d{4})/(?P<month>\d{1,2})/$', 'event_archive', name='event_archive'),
)
