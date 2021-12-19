from django.contrib import admin
from .models import Genre, Album, Music

# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    model = Genre
    list_display = ['genre']

class AlbumAdmin(admin.ModelAdmin):
    class Meta:
        model = Album
        list_display = ['name', 'artiste', 'year', 'cover']

class MusicAdmin(admin.ModelAdmin):
    model = Music
    list_display = ['album', 'title', 'genre', 'artiste', 'audio_file']

admin.site.register(Genre, GenreAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Music, MusicAdmin)