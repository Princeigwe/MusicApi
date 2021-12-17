from django.contrib.auth.models import User
from django.db import models
from rest_framework import serializers
from .models import UserPlaylist, UserPlaylistSong, UserFavourites
from music.serializers import MusicSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer
# from accounts.serializers import UserAccountSerializer


class UserPlayListSongSerializer(WritableNestedModelSerializer):
    # music = MusicSerializer()
    class Meta:
        model = UserPlaylistSong
        fields = ('id', 'user_playlist', 'music',)
    
    # def create(self, validated_data):
    #     music_data = validated_data.pop('music')
    #     music = MusicSerializer.create(MusicSerializer(), validated_data=music_data)
    #     user_playlist_song = UserPlaylistSong.objects.update_or_create(music, user_playlist=validated_data.pop('user_playlist'), id=validated_data.pop('id'))
    #     return user_playlist_song

class  UserPlayListSerializer(serializers.ModelSerializer):
    user_playlist_song = UserPlayListSongSerializer(read_only=True, many=True)
    class Meta:
        model = UserPlaylist
        fields = ['id', 'user', 'name', 'user_playlist_song']

class UserFavouritesSerializer(serializers.ModelSerializer):
    pass