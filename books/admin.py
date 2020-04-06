from django.contrib import admin
from books.models import Publisher, Author, Book, BookImg


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    search_fields = ('last_name', 'first_name')


# Define an inline admin descriptor
class BookImgInline(admin.StackedInline):
    model = BookImg
    can_delete = False
    verbose_name_plural = 'slika'
    classes = ('collapse open',)
    inline_classes = ('collapse open',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    def admin_authors_display(self, obj):
        return unicode(', '.join(unicode(x) for x in obj.authors.all()))
    admin_authors_display.short_description = 'autori'

    def admin_image_display(self, obj):
        if hasattr(obj, 'image'):
            return '<a href="%s"><img src="%s"></a>' % (obj.image.image.url, obj.image.get_admin_thumbnail_url())
        else:
            return ''
    admin_image_display.short_description = 'slika'
    admin_image_display.allow_tags = True

    list_display = ('title', 'publisher', 'admin_authors_display', 'category', 'admin_image_display')
    search_fields = ('title', 'publisher__name', 'authors__first_name', 'authors__last_name')
    list_filter = ('category',)
    filter_horizontal = ('authors',)

    inlines = (BookImgInline,)
