from urllib import request

from django.core.checks import messages
from django.shortcuts import render
from django.views.generic import CreateView

from .models import Contact
from .forms import ContactForm


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):  # ... автоматически добавляет авторизованного юзера в поле authors
        form.instance.added_by = self.request.user
        return super().form_valid(form)
