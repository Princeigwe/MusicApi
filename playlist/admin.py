from django.contrib import admin
from django.db import models
from .models import UserPlaylist, UserPlaylistSong
# Register your models here.

class UserPlaylistSongTabularInline(admin.TabularInline):
    model = UserPlaylistSong
    

class UserPlaylistAdmin(admin.ModelAdmin):
    model = UserPlaylist
    list_display = ['user','name']
    inlines = [UserPlaylistSongTabularInline]

admin.site.register(UserPlaylist, UserPlaylistAdmin)