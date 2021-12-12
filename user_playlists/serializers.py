from django.contrib.auth.models import User
from django.db import models
from rest_framework import fields, serializers
from .models import UserPlaylist, UserPlaylistSong
# from .models import UserFavourites
from music.serializers import MusicSerializer
# from accounts.serializers import UserAccountSerializer


class UserPlayListSongSerializer(serializers.ModelSerializer):
    music = MusicSerializer()
    class Meta:
        model = UserPlaylistSong
        fields = ('id', 'user_playlist', 'music',)

class  UserPlayListSerializer(serializers.ModelSerializer):
    user_playlist_song = UserPlayListSongSerializer(read_only=True, many=True)
    class Meta:
        model = UserPlaylist
        fields = ['id', 'user', 'name', 'user_playlist_song']