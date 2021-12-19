from .models import Genre, Album, Music
from rest_framework import fields, serializers

# to make the model data visible to the api
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id','genre',)

class MusicSerializer(serializers.ModelSerializer):
    # audio_file = serializers.SlugField(min_length=None)
    # title = serializers.CharField()
    # artiste = serializers.CharField()
    genre_id = serializers.IntegerField(write_only=True)
    genre = GenreSerializer(read_only=True)
    audio_file = serializers.FileField()
    class Meta:
        model = Music
        fields = ('id', 'album', 'title', 'genre_id', 'genre', 'artiste', 'audio_file',)

class AlbumSerializer(serializers.ModelSerializer):
    music = MusicSerializer(many=True, read_only=True)
    class Meta:
        model = Album
        fields = ('id', 'name', 'artiste', 'year', 'cover_photo', 'music',)
    
