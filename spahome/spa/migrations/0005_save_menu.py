# Generated by Django 4.1.4 on 2022-12-15 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spa', '0004_alter_body_care_photo_alter_rituals_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Save_menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.FileField(help_text='Это может быть только zip-файл', upload_to='media/', verbose_name='Путь')),
            ],
            options={
                'verbose_name': 'Файл меню для загрузки пользователям',
                'verbose_name_plural': 'Файл меню для загрузки пользователям',
            },
        ),
    ]
