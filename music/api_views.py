from rest_framework import viewsets
from .serializers import GenreSerializer, AlbumSerializer, MusicSerializer
from .models import Genre, Album, Music
from rest_framework import permissions
# from rest_framework.parsers import MultiPartParser

# viewset for GenreSerializer
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filterset_fields = ['genre'] #setting query key for endpoint
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
# viewset for AlbumSerializer
class AlbumViewSet(viewsets.ModelViewSet):
    """ This lists all album resources in the API """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filterset_fields = ['name', 'artiste'] #setting query key for endpoint
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# viewset for MusicSerializer
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    filterset_fields = ['title'] #setting query key for endpoint
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]