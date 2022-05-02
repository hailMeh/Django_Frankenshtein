from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm


class SignUpPageView(generic.CreateView):
    form_class = CustomUserCreationForm  # используется собственная расширенная модель регистрации
    success_url = reverse_lazy('login')  # после успешной регистрации, редирект на url с именем login
    template_name = 'registration/signup.html'
