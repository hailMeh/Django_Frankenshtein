from django import forms
from captcha.fields import CaptchaField
from .models import Contact


class ContactForm(forms.ModelForm):
    """Форма обратной связи по email"""


    class Meta:
        model = Contact
        fields = ("email", 'description')
        widgets = {
            "email": forms.TextInput(attrs={"class": "user_sending_email", "placeholder": "Your Email..."}),
            "description": forms.Textarea(attrs={'rows': 5, 'cols': 25,"class": "user_sending_text", "placeholder": "Your Message..."})

        }
        labels = {
            "email": '',
            "description": ''
        }