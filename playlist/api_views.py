from rest_framework import viewsets, permissions
from rest_framework.decorators import permission_classes
from .models import UserPlaylist, UserPlaylistSong
from .serializers import UserPlayListSerializers, UserPlayListSongSerializer

class UserPlaylistSongViewset(viewsets.ModelViewSet):
    queryset = UserPlaylistSong.objects.all()
    serializer_class = UserPlayListSongSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserPlaylistViewset(viewsets.ModelViewSet):
    queryset = UserPlaylist.objects.all()
    serializer_class = UserPlayListSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]