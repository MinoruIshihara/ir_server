# Generated by Django 4.2 on 2023-08-20 06:24

from django.db import migrations, models
import wallpaper.models


class Migration(migrations.Migration):

    dependencies = [
        ('wallpaper', '0003_alter_image_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to=wallpaper.models.upload_to),
        ),
    ]