from django.contrib.auth.models import User
from django.db import models
from rest_framework import fields, serializers
from .models import UserPlaylist, UserPlaylistSong
# from .models import UserFavourites
from music.serializers import MusicSerializer
from accounts.serializers import UserAccountSerializer
# from djoser.serializers import UserSerializer

# class UserPlayListSongSerializer(serializers.ModelSerializer):
#     music = MusicSerializer()
#     class Meta:
#         model = UserPlaylistSong
#         fields = ('user_playlist', 'music',)

class  UserPlayListSerializer(serializers.ModelSerializer):
    # user = UserAccountSerializer(read_only=True)
    class Meta:
        model = UserPlaylist
        fields = ['id', 'user', 'name']