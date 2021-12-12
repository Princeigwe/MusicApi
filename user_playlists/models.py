from django.db import models
from accounts.models import CustomUser
from music.models import Music
# Create your models here.

class UserPlaylist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user_playlist")
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class UserPlaylistSong(models.Model):
    user_playlist = models.ForeignKey(UserPlaylist, on_delete=models.CASCADE, related_name='user_playlist_song')
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.music.title