from django.views.generic import ListView, DetailView, CreateView
from .models import Music
from .forms import AddMusicForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

class MusicListView(ListView):
    model = Music
    template_name = 'music/music_list.html'
    context_object_name = 'music_list'


class MusicDetailView(DetailView):
    model = Music
    template_name = 'music/music_detail.html'


class AddMusicView(LoginRequiredMixin, CreateView):
    form_class = AddMusicForm
    template_name = 'music/add_music.html'
    success_url = reverse_lazy(
        'music_list')
    raise_exception = True  # Если пользователь неавторизован, то доступ запрещен


def authneed(request, exception):  # Страница не найдена
    return render(request, 'handlers/403.html', {'title': 'Access denied'})