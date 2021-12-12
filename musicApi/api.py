# contains all the API endpoints

from rest_framework import routers
from music.api_views import GenreViewSet, AlbumViewSet, MusicViewSet

router = routers.SimpleRouter()

router.register('genres', GenreViewSet)
router.register('albums', AlbumViewSet)
router.register('music', MusicViewSet)
# router.register('user-playlist', UserPlaylistViewset)
# router.register('user-playlist-song', UserPlaylistSongViewset)
