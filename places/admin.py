from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image

class ImageInlain(admin.TabularInline):
    model = Image
    fields = ['place', 'image', 'get_image_preview', 'order_numb']
    readonly_fields = ['get_image_preview']

    def get_image_preview(self, place):
        return format_html(
            '<img src="{}" width="auto" height="200px" />', place.image.url
        )

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInlain,
    ]

admin.site.register(Image)
