from django.shortcuts import render
from rest_framework import generics
from .models import Music
from .serializers import MusicSerializer
from rest_framework.parsers import MultiPartParser, FileUploadParser
# Create your views here.

class ListOrCreateMusicAPIView(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    parser_classes = [MultiPartParser, FileUploadParser]

class RetrieveOrDeleteMusicAPIView(generics.RetrieveDestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

