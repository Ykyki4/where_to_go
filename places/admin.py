from django.contrib import admin
from .models import Place, Image

class ImageInlain(admin.TabularInline):
    model = Image

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInlain,
    ]

admin.site.register(Image)
