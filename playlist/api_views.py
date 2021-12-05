from rest_framework import serializers, viewsets, permissions
from rest_framework.decorators import permission_classes
from .models import UserPlaylist, UserPlaylistSong, UserFavourites
from .serializers import UserPlayListSerializers, UserPlayListSongSerializer, UserFavouritesSerializer

class UserPlaylistSongViewset(viewsets.ModelViewSet):
    queryset = UserPlaylistSong.objects.all()
    serializer_class = UserPlayListSongSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserPlaylistViewset(viewsets.ModelViewSet):
    queryset = UserPlaylist.objects.all()
    serializer_class = UserPlayListSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserFavouritesViewset(viewsets.ModelViewSet):
    queryset = UserFavourites.objects.all()
    serializer_class = UserFavouritesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]