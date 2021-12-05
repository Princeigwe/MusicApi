from django.contrib.auth.models import User
from django.db import models
from rest_framework import fields, serializers
from .models import UserPlaylist, UserPlaylistSong, UserFavourites
from music.serializers import MusicSerializer
from accounts.serializers import UserCreateSerializer

class UserPlayListSongSerializer(serializers.ModelSerializer):
    music = MusicSerializer()
    class Meta:
        model = UserPlaylistSong
        fields = ('user_playlist', 'music',)

class UserPlayListSerializers(serializers.ModelSerializer):
    user_playlist_song = UserPlayListSongSerializer(many=True, read_only=True)
    user = UserCreateSerializer(read_only=True)
    class Meta:
        model = UserPlaylist
        fields = ('user','name', 'user_playlist_song')

class UserFavouritesSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer(read_only=True)
    music = MusicSerializer()
    class Meta:
        model = UserFavourites
        fields = ('user','music')