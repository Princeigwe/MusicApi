from django.contrib import admin
from django.db import models
from .models import UserPlaylist, UserPlaylistSong, UserFavourites
# Register your models here.

class UserPlaylistSongTabularInline(admin.TabularInline):
    model = UserPlaylistSong
    

class UserPlaylistAdmin(admin.ModelAdmin):
    model = UserPlaylist
    list_display = ['user','name']
    inlines = [UserPlaylistSongTabularInline]


class UserFavouritesAdmin(admin.ModelAdmin):
    model = UserFavourites
    list_display = ['user', 'music']

admin.site.register(UserPlaylist, UserPlaylistAdmin)
admin.site.register(UserFavourites, UserFavouritesAdmin)