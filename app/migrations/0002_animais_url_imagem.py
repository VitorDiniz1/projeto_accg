# Generated by Django 5.0.6 on 2024-06-10 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animais',
            name='url_imagem',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
