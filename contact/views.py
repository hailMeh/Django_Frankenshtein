from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from .models import Contact
from .forms import ContactForm


class ContactView(SuccessMessageMixin, CreateView):
    model = Contact
    form_class = ContactForm
    success_url = "/"
    success_message = "Message was created successfully"

    def form_valid(self, form):  # ... автоматически добавляет авторизованного юзера в поле authors
        form.instance.added_by = self.request.user
        return super().form_valid(form)
