# Generated by Django 4.1.4 on 2022-12-15 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spa', '0003_body_care_rituals_delete_mountain_spa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='body_care',
            name='photo',
            field=models.ImageField(upload_to='static/photo/photo_care/', verbose_name='уходовое фото'),
        ),
        migrations.AlterField(
            model_name='rituals',
            name='photo',
            field=models.ImageField(upload_to='static/photo/photo_rituals/', verbose_name='фото массажа'),
        ),
    ]