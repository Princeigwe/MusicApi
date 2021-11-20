from django.db import models

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
)

class Genre(models.Model):
    genre = models.CharField(max_length=90, choices=GENRES_CHOICES)
    
    def __str__(self):
        return self.genre

class Music(models.Model):
    title = models.CharField(max_length=90)
    artiste = models.CharField(max_length=90)
    # cover_photo = 