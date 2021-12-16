from .models import Genre, Album, Music
from rest_framework import fields, serializers

# to make the model data visible to the api
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('genre',)

class MusicSerializer(serializers.ModelSerializer):
    # audio_file = serializers.SlugField(min_length=None)
    title = serializers.CharField()
    artiste = serializers.CharField()
    audio_file = serializers.FileField(read_only=True)
    class Meta:
        model = Music
        fields = ('id', 'title', 'artiste', 'audio_file',)

class AlbumSerializer(serializers.ModelSerializer):
    music = MusicSerializer(many=True, read_only=True)
    class Meta:
        model = Album
        fields = ('id', 'name', 'artiste', 'year', 'cover_photo', 'music',)
    
