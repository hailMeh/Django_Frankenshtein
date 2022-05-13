from django.views.generic import ListView,DetailView
from .models import Music


class MusicListView(ListView):
    model = Music
    template_name = 'music/music_list.html'
    context_object_name = 'music_list'


class MusicDetailView(DetailView):
    model = Music
    template_name = 'music/music_detail.html'

