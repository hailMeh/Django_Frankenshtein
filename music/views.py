import requests
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import AddMusicForm, ReviewForm, RatingForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Avg


class getYearInClass: # используется вместо контекста и для фильтрации

    def get_year(self):
        return Music.objects.filter(draft=False).values("year") # вернет только поле year из модели music

    def get_category(self):
        return Category.objects.all()

class MusicListView(LoginRequiredMixin, getYearInClass, ListView):
    model = Music
    template_name = 'music/music_list.html'
    paginate_by = 2
    context_object_name = 'music_list'
    raise_exception = True  # Если пользователь неавторизован, то доступ запрещен
    queryset = Music.objects.all().order_by('-time_create').filter(draft=False) # Отображение на главной в обратном порядке. Select_related для оптимизации загрузки из БД

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'All albums'
        return context


class MusicDetailView(LoginRequiredMixin, DetailView):#PermissionRequiredMixin, DetailView):
    model = Music
    template_name = 'music/music_detail.html'
    success_url = reverse_lazy(
        'music_list')
    raise_exception = True  # Если пользователь неавторизован, то доступ запрещен
    #permission_required = 'music.special_status'  # созданный ранее доступ через Meta в моделях

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['music']
        context["star_form"] = RatingForm() # для рейтинга
        context["rating_sum"] = Rating.objects.aggregate(average_star=Avg('star'))
        return context




class AddMusicView(LoginRequiredMixin, CreateView):
    form_class = AddMusicForm
    template_name = 'music/add_music.html'
    success_url = reverse_lazy(
        'music_list')
    raise_exception = True  # Если пользователь неавторизован, то доступ запрещен

    def form_valid(self, form):  # ... автоматически добавляет авторизованного юзера в поле authors
        form.instance.added_by = self.request.user
        return super().form_valid(form)

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


class MusicUpdateView(LoginRequiredMixin, UserPassesTestMixin,
                        UpdateView):  # Миксин не дает гостю зайти на url редактирования сообщений
    model = Music
    template_name = 'music/music_update.html'
    fields = ['title', 'author','price']
    login_url = 'login'  # Редирект на url, если гость неавторизован

    def test_func(self):  # # Не дает изменить сообщение, если оно не своё
        obj = self.get_object()
        return obj.added_by == self.request.user


class MusicDeleteView(LoginRequiredMixin, UserPassesTestMixin,
                        DeleteView):  # Миксин не дает гостю зайти на url удаления сообщения
    model = Music
    template_name = 'music/music_delete.html'
    success_url = reverse_lazy('music_list')
    login_url = 'login'  # Редирект на url, если гость неавторизован

    def test_func(self):  # Не дает удалить сообщение, если оно не своё, работает благодаря миксину UserPassesTestMixin
        obj = self.get_object()
        return obj.added_by == self.request.user


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


class AddReview(View):
    """Отзывы"""
    def post(self, request, pk):
        form = ReviewForm(request.POST) # запрос данных
        music = Music.objects.get(id=pk) # получение айдишника для связи альбома с отзывом
        if form.is_valid(): # провека правильности заполнения формы
            form = form.save(commit=False) # остановка сохранения для проведения манипуляций перед сохранением
            form.music = music # связь альбома с отзывом
            if request.POST.get("parent", None): # для ответов на комменты по родительскому комментарию
                form.parent_id = int(request.POST.get("parent"))
            form.name = request.user
            form.email = request.user.email
            form.save() # и теперь уже сохранение
        return redirect(music.get_absolute_url()) # редирект на альбом к которому был добавлен отзыв


class FilterMusicView(getYearInClass, ListView):
    """Фильтр"""
    paginate_by = 5

    def get_queryset(self):
        queryset = Music.objects.all()
        if "category" in self.request.GET:
            queryset = queryset.filter(category__in=self.request.GET.getlist("category"))
        if "year" in self.request.GET:
            queryset = queryset.filter(year__in=self.request.GET.getlist("year"))
        return queryset


class AddStarRating(View):
    """Добавление рейтинга фильму"""

    def post(self, request): # При запросе
        form = RatingForm(request.POST) # Передадим нашу форму с методом POST
        if form.is_valid(): # Если форма валидна
            Rating.objects.update_or_create( # Рейтинг обновляется если была оценка и создает новую если не было
                added_by = self.request.user, # Передадим авторизованного юзера
                music_id=int(request.POST.get("music")), # Передадим поле альбома к которому рейтинг
                # поле Music_id передается через скрытое поле hidden
                defaults={'star_id': int(request.POST.get("star"))} # Передадим поле альбома к которому рейтинг
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)