from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('django.contrib.flatpages.views',
    url(r'^naslovna/$', 'flatpage', {'url': '/home/'}, name='home'),

    url(r'^kampanja/$', 'flatpage', {'url': '/about/'}, name='about'),
    url(r'^partneri/$', 'flatpage', {'url': '/partners/'}, name='partners'),
    url(r'^suradnici/$', 'flatpage', {'url': '/associates/'}, name='associates'),
    url(r'^materijali/$', 'flatpage', {'url': '/materials/'}, name='materials'),

    url(r'^predstavljanje-kampanje/$', 'flatpage', {'url': '/campain-start/'}, name='campain_start'),

    url(r'^citanje-naglas/$', 'flatpage', {'url': '/reading-aloud/'}, name='reading_aloud'),
    url(r'^razvoj-djeteta/$', 'flatpage', {'url': '/child-development/'}, name='child_development'),
    url(r'^citanje-s-pedijatrima/$', 'flatpage', {'url': '/reading-paediatrician/'}, name='reading_paediatrician'),

    url(r'^slikovnica/$', 'flatpage', {'url': '/books-about/'}, name='books_about'),
    url(r'^slikovnica-i-dijete/$', 'flatpage', {'url': '/books-and-child/'}, name='books_and_child'),

    url(r'^pravila-nagradne-igre/$', 'flatpage', {'url': '/contest-rules/'}, name='contest_rules'),
    url(r'^slikovnica-tjedna/$', 'flatpage', {'url': '/contest-prize/'}, name='contest_prize'),
)
