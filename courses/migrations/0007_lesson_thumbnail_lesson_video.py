# Generated by Django 5.2 on 2025-05-07 02:08

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_lesson_preview_lesson_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='thumbnail',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='video',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='video'),
        ),
    ]
