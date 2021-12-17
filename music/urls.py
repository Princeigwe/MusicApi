from django.urls import path
from .views import ListOrCreateMusicAPIView, RetrieveOrDeleteMusicAPIView

urlpatterns = [
    path('', ListOrCreateMusicAPIView.as_view()), 
    path('<int:pk>/', RetrieveOrDeleteMusicAPIView.as_view())
]