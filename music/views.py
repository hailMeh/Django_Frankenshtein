from django.views.generic import ListView, DetailView, CreateView
from .models import Music
from .forms import AddMusicForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

class MusicListView(LoginRequiredMixin, ListView):
    model = Music
    template_name = 'music/music_list.html'
    paginate_by = 2
    context_object_name = 'music_list'
    raise_exception = True  # Если пользователь неавторизован, то доступ запрещен


class MusicDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Music
    template_name = 'music/music_detail.html'
    success_url = reverse_lazy(
        'music_list')
    raise_exception = True  # Если пользователь неавторизован, то доступ запрещен
    permission_required = 'music.special_status'  # созданный ранее доступ через Meta в моделях


class AddMusicView(LoginRequiredMixin, CreateView):
    form_class = AddMusicForm
    template_name = 'music/add_music.html'
    success_url = reverse_lazy(
        'music_list')
    raise_exception = True  # Если пользователь неавторизован, то доступ запрещен


def authneed(request, exception):  # Страница не найдена
    return render(request, 'handlers/403.html', {'title': 'Access denied'})


class SearchResultsListView(ListView):
    model = Music
    template_name = 'music/search_results.html'
    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        return Music.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
