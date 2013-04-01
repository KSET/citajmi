# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from gallery.models import Album, AlbumEntry, EntryImg

class EntryAlbumFilter(SimpleListFilter):
    # Human-readable title which will be displayed in the filter sidebar
    title = 'svrstan u album'
    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'albums'

    def lookups(self, request, model_admin):
        return [('True', 'Da'), ('False', 'Ne')]

    def queryset(self, request, queryset):
        albums = self.value()
        if albums == 'True':
            return queryset.exclude(albums=None)
        elif albums == 'False':
            return queryset.filter(albums=None)
        else:
            return queryset


class EntryTypeFilter(SimpleListFilter):
    # Human-readable title which will be displayed in the filter sidebar
    title = 'slika/video'
    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'image'

    def lookups(self, request, model_admin):
        return [('True', 'Slika'), ('False', 'Video')]

    def queryset(self, request, queryset):
        image = self.value()
        if image == 'True':
            return queryset.exclude(image=None)
        elif image == 'False':
            return queryset.filter(image=None)
        else:
            return queryset


# Define an inline admin descriptor
class EntryImgInline(admin.StackedInline):
    model = EntryImg
    can_delete = False
    verbose_name_plural = 'slika'
    classes = ('collapse open',)
    inline_classes = ('collapse open',)


class AlbumEntryAdmin(admin.ModelAdmin):
    def admin_album_display(self, obj):
        return unicode(', '.join(unicode(x) for x in obj.albums.all()))
    admin_album_display.short_description = 'albumi'

    def admin_image_display(self, obj):
        url = obj.get_thumbnail_url(big=False)
        if obj.video:
            return '<a href="%s"><img style="width: 60px;" src="%s"></a>' % (obj.video, url)
        else:
            return '<a href="%s"><img src="%s"></a>' % (obj.image.image.url, url)
    admin_image_display.short_description = 'link'
    admin_image_display.allow_tags = True

    def admin_type_display(self, obj):
        return bool(obj.video)
    admin_type_display.short_description = 'video'
    admin_type_display.admin_order_field  = 'video'
    admin_type_display.boolean = True

    list_display = ('created', 'full_name', 'public', 'cover', 'admin_album_display', 'admin_type_display', 'admin_image_display')
    search_fields = ('full_name',)
    list_filter = ('public', 'cover', EntryAlbumFilter, EntryTypeFilter, 'created')
    date_hierarchy = 'created'

    inlines = (EntryImgInline,)

admin.site.register(AlbumEntry, AlbumEntryAdmin)


class AlbumAdmin(admin.ModelAdmin):
    def admin_cover_display(self, obj):
        url = obj.get_cover_url(big=False)
        if 'youtube' in url:
            return '<img style="width: 60px;" src="%s"></a>' % (url,)
        else:
            return '<img src="%s"></a>' % (url,)
    admin_cover_display.short_description = 'naslovna slika'
    admin_cover_display.allow_tags = True

    list_display = ('title', 'date', 'public', 'admin_cover_display')
    search_fields = ('title',)
    list_filter = ('public', 'date')
    date_hierarchy = 'date'

    def get_object(self, request, object_id):
        # Hook obj for use in formfield_for_manytomany
        self.obj = super(AlbumAdmin, self).get_object(request, object_id)
        return self.obj

    filter_horizontal = ('entries',)
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'entries':
            kwargs['queryset'] = AlbumEntry.objects.filter(public=True, albums=None)
            if hasattr(self, 'obj'):
                kwargs['queryset'] = kwargs['queryset'].all() | self.obj.entries.all()
        return super(AlbumAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

    fieldsets = (
        (None, {
            'fields': ('title', 'date', 'entries', 'public'),
            'description': u'Za album se mogu izabrati samo stavke albuma (slika/video) koje su odobrene i koje ne pripadaju ni jednom drugom albumu.',
        }),
    )

admin.site.register(Album, AlbumAdmin)
