from django.contrib import admin
from events.models import Event, EventImg

# Define an inline admin descriptor
class EventImgInline(admin.StackedInline):
    model = EventImg
    can_delete = False
    verbose_name_plural = 'slika'
    classes = ('collapse open',)
    inline_classes = ('collapse open',)

class EventAdmin(admin.ModelAdmin):
    def admin_image_display(self, obj):
        if hasattr(obj, 'image'):
            return '<a href="%s"><img src="%s"></a>' % (obj.image.image.url, obj.image.get_admin_thumbnail_url())
        else:
            return ''
    admin_image_display.short_description = 'slika'
    admin_image_display.allow_tags = True

    list_display = ('title', 'created', 'start', 'location', 'public', 'admin_image_display')
    search_fields = ('title', 'location', 'info')
    list_filter = ('public', 'created')
    date_hierarchy = 'start'

    ordering = ['-created']

    inlines = (EventImgInline,)

admin.site.register(Event, EventAdmin)
