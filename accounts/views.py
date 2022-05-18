from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.shortcuts import redirect

class SignUpPageView(generic.CreateView):
    form_class = CustomUserCreationForm  # используется собственная расширенная модель регистрации
    success_url = reverse_lazy('login')  # после успешной регистрации, редирект на url с именем login
    template_name = 'registration/signup.html'

    def form_valid(self, form):  # Авторизация сразу после регистрации
        user = form.save()
        login(self.request, user)
        return redirect('home')

    def get_context_data(self, *, object_list=None, **kwargs):  # любой контекст для отображения в шаблоне
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registration'
        return context