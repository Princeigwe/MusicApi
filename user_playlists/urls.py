from django.urls import path
from .views import (ListOrCreateUserPlaylistsAPIView,
                    RetrieveOrDeleteUserPlaylistAPIView,
                    ListOrCreateUserPlaylistSongAPIView,
                    RetrieveOrDeleteUserPlaylistSongAPIView,
                    ListOrCreateUserFavouritesAPIView,
                    RetrieveOrDeleteUserFavouritesAPIView)

urlpatterns = [
    path('', ListOrCreateUserPlaylistsAPIView.as_view()),
    path('<int:pk>/', RetrieveOrDeleteUserPlaylistAPIView.as_view()),
    path('songs/', ListOrCreateUserPlaylistSongAPIView.as_view(),),
    path('songs/<int:pk>/', RetrieveOrDeleteUserPlaylistSongAPIView.as_view(),),
    path('favourites/', ListOrCreateUserFavouritesAPIView.as_view()),
    path('favourites/<int:pk>/', RetrieveOrDeleteUserFavouritesAPIView.as_view()),
]