from django import template
from music.models import *

# Пользовательские таги для принципа DRY

register = template.Library()


@register.simple_tag()  # Загружай категории книг, используй данный тэг в base.html и можно использовать в любом шаблоне
def get_categories():
    return Category.objects.all()

