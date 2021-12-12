from django.urls import path
from .views import ListOrCreateUserPlaylistsAPIView, RetrieveOrDeleteUserPlaylistAPIView

urlpatterns = [
    path('', ListOrCreateUserPlaylistsAPIView.as_view()),
    path('<int:pk>/', RetrieveOrDeleteUserPlaylistAPIView.as_view(),)
]