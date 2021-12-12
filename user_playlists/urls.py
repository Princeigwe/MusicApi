from django.urls import path
from .views import (ListOrCreateUserPlaylistsAPIView,
                    RetrieveOrDeleteUserPlaylistAPIView,
                    ListOrCreateUserPlaylistSongAPIView,
                    RetrieveOrDeleteUserPlaylistSongAPIView)

urlpatterns = [
    path('', ListOrCreateUserPlaylistsAPIView.as_view()),
    path('<int:pk>/', RetrieveOrDeleteUserPlaylistAPIView.as_view()),
    path('songs/', ListOrCreateUserPlaylistSongAPIView.as_view(),),
    path('songs/<int:pk>/', RetrieveOrDeleteUserPlaylistSongAPIView.as_view(),)
]