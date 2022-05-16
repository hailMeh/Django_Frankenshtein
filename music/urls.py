from django.urls import path
from .views import MusicListView, MusicDetailView, AddMusicView, SearchResultsListView
urlpatterns = [
    path('', MusicListView.as_view(), name='music_list'),
    path('<slug:slug>/', MusicDetailView.as_view(), name='music_detail'),
    path('addmusic/', AddMusicView.as_view(), name='music_add'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
]
