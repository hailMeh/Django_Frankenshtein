from django import forms
from django.core.exceptions import ValidationError
from .models import *
from captcha.fields import CaptchaField


class AddMusicForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Music
        fields = ['title', 'author','category','price', 'cover', 'slug']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def clean_title(self):   #  Пользовательские ограничения в форме
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Length is more than 200 keywords')
        return title
