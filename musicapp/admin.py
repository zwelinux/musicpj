from django.contrib import admin
from .models import Artist, Song, Playlist, Album
# Register your models here.

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['name', 'date']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}