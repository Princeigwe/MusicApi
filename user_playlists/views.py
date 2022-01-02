from django.shortcuts import render
from rest_framework import generics, serializers
from rest_framework import parsers
from .models import UserPlaylist, UserPlaylistSong, UserFavourites
from .serializers import UserPlayListSerializer, UserPlayListSongSerializer, UserFavouritesSerializer
from .permissions import PlaylistOwnerOrAdmin, PlaylistSongOwnerOrAdmin, FavouritesOwnerOrAdmin
from rest_framework.parsers import MultiPartParser, JSONParser, FileUploadParser

# Create your views here.

class ListOrCreateUserPlaylistsAPIView(generics.ListCreateAPIView):
    """ 
    This returns a list of the authorized user's playlists.
    """
    queryset = UserPlaylist.objects.all()
    serializer_class = UserPlayListSerializer
    permission_classes = [PlaylistOwnerOrAdmin]

class RetrieveOrDeleteUserPlaylistAPIView(generics.RetrieveDestroyAPIView):
    queryset = UserPlaylist.objects.all()
    serializer_class = UserPlayListSerializer
    permission_classes = [PlaylistOwnerOrAdmin]

class ListOrCreateUserPlaylistSongAPIView(generics.ListCreateAPIView):
    """
    This returns the list of the authorized user playlist's songs.
    """
    queryset = UserPlaylistSong.objects.all()
    serializer_class = UserPlayListSongSerializer
    parser_classes = [MultiPartParser, FileUploadParser]
    permission_classes = [PlaylistSongOwnerOrAdmin]

class RetrieveOrDeleteUserPlaylistSongAPIView(generics.RetrieveDestroyAPIView):
    queryset = UserPlaylistSong.objects.all()
    serializer_class = UserPlayListSongSerializer
    permission_classes = [PlaylistSongOwnerOrAdmin]

class ListOrCreateUserFavouritesAPIView(generics.ListCreateAPIView):
    """
    This returns a list of authenticated user's favourites. This is only available for the authorized user
    """
    queryset = UserFavourites.objects.all()
    serializer_class = UserFavouritesSerializer
    permission_classes = [FavouritesOwnerOrAdmin]

class RetrieveOrDeleteUserFavouritesAPIView(generics.RetrieveDestroyAPIView):
    queryset = UserFavourites.objects.all()
    serializer_class = UserFavouritesSerializer
    permission_classes = [FavouritesOwnerOrAdmin]