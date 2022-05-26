from django import forms
from django.core.exceptions import ValidationError
from .models import *
from captcha.fields import CaptchaField


class AddMusicForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Music
        fields = ['title', 'author','category','price', 'cover']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
        }


    def clean_title(self):   #  Пользовательские ограничения в форме
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Length is more than 200 keywords')
        return title



class ReviewForm(forms.ModelForm):
    """Форма отзывов"""

    class Meta:
        model = Reviews
        fields = ("text",)
        widgets = {


            "text": forms.Textarea(attrs={"class": "form-control border"})
        }


class RatingForm(forms.ModelForm):
    """Форма добавления рейтинга"""
    star = forms.ModelChoiceField( # переопределение поля star, в виджетах также могут быть другие чекбоксы и кнопки
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ("star",)