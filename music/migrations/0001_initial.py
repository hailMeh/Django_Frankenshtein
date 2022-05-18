# Generated by Django 4.0.4 on 2022-05-18 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категории',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200, verbose_name='Title')),
                ('author', models.CharField(max_length=200, verbose_name='Author')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('cover', models.ImageField(blank=True, upload_to='covers/')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='music.category')),
            ],
            options={
                'verbose_name': 'Музыка',
                'verbose_name_plural': 'Альбомы',
                'ordering': ['time_create', 'title', 'author', 'category'],
                'permissions': [('special_status', 'Can check all music')],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('music', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='music.music')),
            ],
        ),
    ]
