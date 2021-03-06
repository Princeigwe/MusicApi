from django.db import models
# from audiofield.fields import AudioField
from django.conf import settings

# Create your models here.

GENRES_CHOICES = (
    ('ROCK', 'Rock'),
    ('POP MUSIC', 'Pop Music'),
    ('HIPHOP MUSIC', 'Hip Hop Music'),
    ('ELECTRONIC DANCE MUSIC', 'Electronic Dance Music'),
    ('CLASSICAL MUSIC', 'Classical Music'),
    ('HOUSE MUSIC', 'House Music'),
    ('TRAP MUSIC', 'Trap Music'),
    ('JAZZ', 'Jazz'),
    ('R&B', 'R&B'),
)

class Genre(models.Model):
    genre = models.CharField(max_length=90, choices=GENRES_CHOICES)
    
    def __str__(self):
        return self.genre

class Album(models.Model):
    name = models.CharField(max_length=300)
    artiste = models.CharField(max_length=300)
    year = models.DateField(auto_now_add=False)
    cover_photo = models.ImageField(upload_to = 'covers/')
    
    def __str__(self):
        return(self.name + " " + str(self.year) + " " + self.artiste)

class Music(models.Model):
    album = models.ForeignKey(Album, related_name='music', on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name='genre_music')
    artiste = models.CharField(max_length=500)
    audio_file = models.FileField(upload_to = 'audio/')
    
    class Meta:
        verbose_name_plural = "Music"
    
    def __str__(self):
        return (self.title + " - " + self.artiste)
