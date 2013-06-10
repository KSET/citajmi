# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django_extensions.db.fields import AutoSlugField
from photologue.models import ImageModel


class EventManager(models.Manager):
    def current(self):
        from django.db.models import Q
        from django.utils import timezone
        qs = self.filter(Q(public=True) & Q(end__gt=timezone.now().date()))
        if not qs.exists():
            qs = self.filter(Q(public=True))[:4]
        return qs.order_by('-created')

    def month(self, year, month):
        from django.db.models import Q
        return self.filter(Q(public=True) & Q(start__year=year) & Q(start__month=month))


class Event(models.Model):
    title = models.CharField('naziv događanja', max_length=50)
    slug = AutoSlugField('slug', max_length=50, unique=True, populate_from=('title',))
    email = models.EmailField('kontakt email')
    start = models.DateTimeField('početak')
    end = models.DateTimeField('kraj')
    location = models.CharField('grad/naselje', max_length=100)
    info = models.TextField('opis', max_length=2000)
    public = models.BooleanField('odobren', default=False, help_text='Da li je događaj objavljen na stranici')
    created = models.DateTimeField('vrijeme kreiranja', blank=True, default=timezone.now)
    objects = EventManager()
    class Meta:
        ordering = ['start', 'created']
        verbose_name = 'događaj'
        verbose_name_plural = 'događaji'
    def __unicode__(self):
        return self.title


class EventImg(ImageModel):
    event = models.OneToOneField(Event, verbose_name='događaj', related_name='image')
    class Meta:
        verbose_name = 'slika'
        verbose_name_plural = 'slike'
    def __unicode__(self):
        return unicode(self.event)
