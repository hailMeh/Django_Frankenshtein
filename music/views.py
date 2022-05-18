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
    queryset = Music.objects.all().order_by('-time_create') # Отображение на главной в обратном порядке. Select_related для оптимизации загрузки из БД

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'All albums'
        return context


class MusicDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Music
    template_name = 'music/music_detail.html'
    success_url = reverse_lazy(
        'music_list')
    raise_exception = True  # Если пользователь неавторизован, то доступ запрещен
    permission_required = 'music.special_status'  # созданный ранее доступ через Meta в моделях

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['music']
        return context


class AddMusicView(LoginRequiredMixin, CreateView):
    form_class = AddMusicForm
    template_name = 'music/add_music.html'
    success_url = reverse_lazy(
        'music_list')
    raise_exception = True  # Если пользователь неавторизован, то доступ запрещен

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add new album'
        return context


def authneed(request, exception):  # Страница не найдена
    return render(request, 'handlers/403.html', {'title': 'Access denied'})


class SearchResultsListView(ListView):
    model = Music
    template_name = 'music/search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        return Music.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))


class CategoryView(ListView):
    model = Music
    template_name = 'music/music_category.html'
    context_object_name = 'music'  # обращение к модели через
    allow_empty = False  # Если пусто то на 404
    paginate_by = 2  # пагинация в base.html

    def get_context_data(self, *, object_list=None, **kwargs):  # Шаблонная запись для изменения/отображения, гибко!
        context = super().get_context_data(**kwargs)
        context['title'] = 'Category - ' + str(context['music'][0].category)
        context['category'] = Music.objects.filter(category__slug=self.kwargs['slug']).select_related('category')
        context['numbers_of_albums'] = Music.objects.filter(category__slug=self.kwargs['slug']).select_related('category').count()
        return context

    def get_queryset(self):  # ОРМ можно применять через служебную функцию
        return Music.objects.filter(category__slug=self.kwargs['slug'], is_published=True).select_related('category')


''' ФУНКЦИОНАЛЬНАЯ ФОРМА ДЛЯ ДОБАВЛЕНИЯ КНИГИ
def addbook(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddBookForm()
    context = {
        'title': 'add_book',
        'form': form
    }
    return render(request, 'women/add_book.html', context=context)
'''