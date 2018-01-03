from django.contrib import admin
from imager_images.models import Photo, Album

admin.site.register(Photo)


class AlbumInline(admin.TabularInline):
    model = Album.photos.through


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = (AlbumInline,)
    exclude = ('photos',)