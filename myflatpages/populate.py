#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

# populate db with predifined flatpages
def main():
    from django.contrib.flatpages.models import FlatPage
    from django.contrib.sites.models import Site
    site, created = Site.objects.get_or_create(domain='citajmi.info', name='citajmi.info')
    stub_text='<h3>Podstranica u izradi</h3><p>Posjetite ju ponovo za par dana!</p>'
    pages = (
        FlatPage(url='/home/', template_name='flatpages/home.html', title=u'Naslovna', content=stub_text),

        FlatPage(url='/about/', title=u'O Kampanji', content=stub_text),
        FlatPage(url='/about-eng/', title=u'Campaign', content=stub_text),
        FlatPage(url='/partners/', title=u'Partneri', content=stub_text),
        FlatPage(url='/associates/', title=u'Suradnici', content=stub_text),
        FlatPage(url='/sponsors/', title=u'Pokrovitelji', content=stub_text),
        FlatPage(url='/materials/', title=u'Materijali - Preuzmite materijale', content=stub_text),

        FlatPage(url='/campain-start/', title=u'Predstavljanje kampanje', content=stub_text),

        FlatPage(url='/reading-aloud/', title=u'Čitanje naglas', content=stub_text),
        FlatPage(url='/child-development/', title=u'Kalendar razvoja djeteta', content=stub_text),
        FlatPage(url='/reading-paediatrician/', title=u'Čitajmo naglas s pedijatrima', content=stub_text),

        FlatPage(url='/books-about/', title=u'O Slikovnici', content=stub_text),
        FlatPage(url='/books-and-child/', title=u'Slikovnica i dijete', content=stub_text),

        FlatPage(url='/contest-rules/', title=u'Pravila nagradne igre', content=stub_text),
        FlatPage(url='/contest-prize/', title=u'Slikovnica tjedna', content=stub_text),
    )
    counter = 0
    for page in pages:
        if not FlatPage.objects.filter(url=page.url).exists():
            page.save()
            page.sites.add(site)
            print 'Created: %s' % page.url
            counter += 1
        else:
            print 'Not created: %s' % page.url
    print 'Created %d flatpages.' % counter

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "citajmi.settings")
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    PROJECT_DIR = os.path.abspath(os.path.join(BASE_DIR, '..'))
    if PROJECT_DIR not in sys.path:
        sys.path.append(PROJECT_DIR)
    main()
