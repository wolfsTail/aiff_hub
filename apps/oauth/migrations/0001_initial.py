# Generated by Django 5.0.1 on 2024-01-17 17:16

import apps.base.services
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=128, unique=True, verbose_name='Email')),
                ('join_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('country', models.CharField(blank=True, max_length=32, null=True, verbose_name='Страна проживания')),
                ('city', models.CharField(blank=True, max_length=32, null=True, verbose_name='Город проживания')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='О себе')),
                ('display_name', models.CharField(blank=True, max_length=32, null=True, verbose_name='Username')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=apps.base.services.get_path_upload_avatar, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png']), apps.base.services.validate_size_image], verbose_name='Аватар')),
            ],
        ),
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribers', to='oauth.authuser', verbose_name='Подписчик')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='oauth.authuser', verbose_name='Владелец')),
            ],
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_links', to='oauth.authuser', verbose_name='Владелец')),
            ],
        ),
    ]