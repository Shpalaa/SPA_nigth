# Generated by Django 3.2.16 on 2022-12-12 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spa', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mountain_spa',
            options={'verbose_name': 'объявление (вид массажа)', 'verbose_name_plural': 'Виды массажей и их стоимость'},
        ),
        migrations.AlterField(
            model_name='mountain_spa',
            name='content',
            field=models.CharField(max_length=250, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='mountain_spa',
            name='photo',
            field=models.ImageField(default='spa/static/', upload_to='templates/static/', verbose_name='фото массажа'),
        ),
        migrations.AlterField(
            model_name='mountain_spa',
            name='price',
            field=models.CharField(blank=True, max_length=50, verbose_name='цена в формате x/x/x'),
        ),
        migrations.AlterField(
            model_name='mountain_spa',
            name='time',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='время в формате x/x/x'),
        ),
        migrations.AlterField(
            model_name='mountain_spa',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
    ]
