from django.shortcuts import render
from rest_framework import generics, serializers
from rest_framework import parsers
from .models import UserPlaylist, UserPlaylistSong
from .serializers import UserPlayListSerializer, UserPlayListSongSerializer
from .permissions import PlaylistOwnerOrAdmin, PlaylistSongOwnerOrAdmin
from rest_framework.parsers import MultiPartParser, JSONParser, FileUploadParser

# Create your views here.

class ListOrCreateUserPlaylistsAPIView(generics.ListCreateAPIView):
    queryset = UserPlaylist.objects.all()
    serializer_class = UserPlayListSerializer
    permission_classes = [PlaylistOwnerOrAdmin]

class RetrieveOrDeleteUserPlaylistAPIView(generics.RetrieveDestroyAPIView):
    queryset = UserPlaylist.objects.all()
    serializer_class = UserPlayListSerializer
    permission_classes = [PlaylistOwnerOrAdmin]

class ListOrCreateUserPlaylistSongAPIView(generics.ListCreateAPIView):
    queryset = UserPlaylistSong.objects.all()
    serializer_class = UserPlayListSongSerializer
    parser_classes = [MultiPartParser, FileUploadParser]
    permission_classes = [PlaylistSongOwnerOrAdmin]

class RetrieveOrDeleteUserPlaylistSongAPIView(generics.RetrieveDestroyAPIView):
    queryset = UserPlaylistSong.objects.all()
    serializer_class = UserPlayListSongSerializer
    permission_classes = [PlaylistSongOwnerOrAdmin]