from django.contrib.auth.models import User
from django.db import models
from rest_framework import serializers
from .models import UserPlaylist, UserPlaylistSong, UserFavourites
from music.serializers import MusicSerializer
from accounts.serializers import UserAccountSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer
# from accounts.serializers import UserAccountSerializer


class UserPlayListSongSerializer(WritableNestedModelSerializer):
    music_id = serializers.IntegerField(write_only=True)
    # user_playlist_id = serializers.IntegerField(write_only=True)
    music = MusicSerializer(read_only=True)
    class Meta:
        model = UserPlaylistSong
        fields = ('id', 'user_playlist', 'music', 'music_id')
    
    # def create(self, validated_data):
    #     music_data = validated_data.pop('music')
    #     music = MusicSerializer.create(MusicSerializer(), validated_data=music_data)
    #     user_playlist_song = UserPlaylistSong.objects.update_or_create(music, user_playlist=validated_data.pop('user_playlist'), id=validated_data.pop('id'))
    #     return user_playlist_song

class  UserPlayListSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)
    user = UserAccountSerializer(read_only=True)
    user_playlist_song = UserPlayListSongSerializer(read_only=True, many=True)
    class Meta:
        model = UserPlaylist
        fields = ['id', 'user_id', 'user', 'name', 'user_playlist_song']

class UserFavouritesSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)
    user = UserAccountSerializer(read_only=True)
    music_id = serializers.IntegerField(write_only=True)
    music = MusicSerializer(read_only=True)
    class Meta:
        model = UserFavourites
        fields = ['id', 'user', 'music',  'music_id', 'user_id']