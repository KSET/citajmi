# -*- coding: utf-8 -*-
from django.db import models
from photologue.models import ImageModel

class Publisher(models.Model):
    name = models.CharField('naziv', max_length=30, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = u'izdavač'
        verbose_name_plural = u'izdavači'
    def __unicode__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField('ime', max_length=30)
    last_name = models.CharField('prezime', max_length=30)

    @property
    def full_name(self):
        "Returns the person's full name."
        return u'%s %s' % (self.first_name, self.last_name)

    class Meta:
        unique_together = ('last_name', 'first_name',)
        ordering = ['last_name', 'first_name']
        verbose_name = 'autor'
        verbose_name_plural = 'autori'
    def __unicode__(self):
        return self.full_name

class Book(models.Model):
    CATEGORY = {1: u'Bebe', 2: u'Djeca mlađeg uzrasta', 3: u'Pjesmarice'}
    title = models.CharField('naslov', max_length=100)
    authors = models.ManyToManyField(Author, verbose_name='autori', related_name='books', blank=True, null=True)
    publisher = models.ForeignKey(Publisher, verbose_name='izdavač', related_name='books')
    category = models.IntegerField('kategorija', choices=CATEGORY.items())
    url = models.URLField('url', help_text='Link na knjigu na stranici izdavača')
    info = models.TextField('opis', max_length=500, blank=True, null=True, help_text='Sažetak, prikaže se prvih 50 riječi.')
    class Meta:
        ordering = ['title']
        verbose_name = 'knjiga'
        verbose_name_plural = 'knjige'
    def __unicode__(self):
        return self.title

class BookImg(ImageModel):
    book = models.OneToOneField(Book, verbose_name='knjiga', related_name='image')
    class Meta:
        verbose_name = 'slika'
        verbose_name_plural = 'slike'
    def __unicode__(self):
        return unicode(self.book)
