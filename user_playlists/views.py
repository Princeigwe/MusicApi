from django.shortcuts import render
from rest_framework import generics
from .models import UserPlaylist
from .serializers import UserPlayListSerializer
from .permissions import PlaylistOwnerOrAdmin

# Create your views here.

class ListOrCreateUserPlaylistsAPIView(generics.ListCreateAPIView):
    queryset = UserPlaylist.objects.all()
    serializer_class = UserPlayListSerializer
    permission_classes = [PlaylistOwnerOrAdmin]

class RetrieveOrDeleteUserPlaylistAPIView(generics.RetrieveDestroyAPIView):
    queryset = UserPlaylist.objects.all()
    serializer_class = UserPlayListSerializer
    permission_classes = [PlaylistOwnerOrAdmin]