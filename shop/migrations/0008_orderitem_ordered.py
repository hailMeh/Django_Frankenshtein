# Generated by Django 4.0.5 on 2022-06-11 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_orderitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
    ]