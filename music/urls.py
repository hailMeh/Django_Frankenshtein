from django.urls import path
from .views import MusicListView, MusicDetailView, AddMusicView, SearchResultsListView, CategoryView, MusicUpdateView, MusicDeleteView,AddReview,FilterMusicView, AddStarRating

urlpatterns = [
    path('', MusicListView.as_view(), name='music_list'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('addmusic/', AddMusicView.as_view(), name='music_add'),
    path("add-rating/", AddStarRating.as_view(), name='add_rating'),
    path("filter/", FilterMusicView.as_view(), name='filter'), # Обязательно перед слаговскими вещами
    path('album/<slug:slug>/', MusicDetailView.as_view(), name='music_detail'),  # Важно чтобы слаг был внизу
    path('category/<slug:slug>/', CategoryView.as_view(), name='category'),
    path('album/<slug:slug>/edit/', MusicUpdateView.as_view(), name='music_update'),
    path('album/<slug:slug>/delete/', MusicDeleteView.as_view(), name='music_delete'),
    path('reviews/<int:pk>', AddReview.as_view(), name='add_review'),

]
