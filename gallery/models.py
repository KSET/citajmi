# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from photologue.models import ImageModel
from gallery.templatetags.custom_filters import youtube_thumbnail_url


class AlbumEntry(models.Model):
    full_name = models.CharField('ime i prezime', max_length=60)
    address = models.CharField('adresa', max_length=100)
    email = models.EmailField('kontakt email')
    video = models.URLField('video snimka', blank=True, null=True,
                            help_text='Internet adresa (link) vaše video snimke na YouTube-u')
    cover = models.BooleanField('naslovna', default=False, help_text='Da li slika/video predstavlja cijeli album')
    public = models.BooleanField('odobren', default=False, help_text='Da li je unos objavljen u albumu')
    created = models.DateTimeField('vrijeme kreiranja', blank=True, default=timezone.now)

    def get_thumbnail_url(self, big=True):
        if self.video:
            return youtube_thumbnail_url(self.video, big)
        else:
            return self.image.get_gallery_thumbnail_url() if big else self.image.get_admin_thumbnail_url()

    class Meta:
        ordering = ['-created']
        verbose_name = 'stavka albuma'
        verbose_name_plural = 'stavke albuma'

    def __unicode__(self):
        return u'[%s] %s (%s)' % (self.created.strftime('%Y-%m-%d'), self.full_name, 'video' if self.video else 'slika')


class EntryImg(ImageModel):
    entry = models.OneToOneField(AlbumEntry, verbose_name='stavka albuma', related_name='image')

    class Meta:
        verbose_name = 'slika'
        verbose_name_plural = 'slike'

    def __unicode__(self):
        return unicode(self.entry)


class Album(models.Model):
    title = models.CharField('naslov', max_length=60)
    date = models.DateField('datum', default=timezone.now)
    entries = models.ManyToManyField(AlbumEntry, verbose_name='stavke albuma', related_name='albums')
    public = models.BooleanField('vidljiv', default=False, help_text='Da li je album objavljen na stranici')

    def get_cover_url(self, big=True):
        qs = self.get_images().filter(cover=True)
        if not qs.exists():
            qs = self.get_videos().filter(cover=True)
        if not qs.exists():
            qs = self.get_images()
        if not qs.exists():
            qs = self.get_videos()
        if qs.exists():
            return qs[0].get_thumbnail_url(big)
        return ''

    def get_videos(self):
        return self.entries.filter(image=None)

    def get_images(self):
        return self.entries.exclude(image=None)

    class Meta:
        ordering = ['-date']
        verbose_name = u'album'
        verbose_name_plural = u'albumi'

    def __unicode__(self):
        return u'[%s] %s' % (self.date.strftime('%Y-%m-%d'), self.title)
