# Generated by Django 4.1.7 on 2023-09-13 18:31

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_author_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featuredImage',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
