from .models import Genre, Album, Music
from rest_framework import fields, serializers

# to make the model data visible to the api
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('genre',)


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('name', 'artiste', 'year', 'cover_photo',)

class MusicSerializer(serializers.ModelSerializer):
    album = AlbumSerializer()
    class Meta:
        model = Music
        fields = ('album', 'title', 'artiste', 'audio_file',)