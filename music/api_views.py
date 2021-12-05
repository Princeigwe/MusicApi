from rest_framework import viewsets
from .serializers import GenreSerializer, AlbumSerializer, MusicSerializer
from .models import Genre, Album, Music
from rest_framework import permissions

# viewset for GenreSerializer
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
# viewset for AlbumSerializer
class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# viewset for MusicSerializer
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]