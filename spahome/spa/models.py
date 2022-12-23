from django.db import models
from datetime import datetime


class Mountain_Rituals(models.Model):
    photo = models.ImageField(upload_to='static/photo/photo_rituals/', verbose_name='фото массажа')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.CharField(max_length=250, verbose_name='описание')
    time = models.CharField(max_length=50, null=True, blank=True, verbose_name='время в формате x/x/x')
    price = models.CharField(max_length=50, null=False, blank=True, verbose_name='цена в формате x/x/x')
    popular = models.BooleanField(default=False, verbose_name='Добавить на главную страницу сайта (популярные массажи)')
    time_create = models.DateTimeField(verbose_name="Время создания", default=datetime.now(), )
    time_update = models.DateTimeField(verbose_name="Время изменения", default=datetime.now(), )

    class Meta:
        verbose_name_plural = 'Mountain-SPA (Виды массажа)'
        verbose_name = 'SPA-ритуалы (вид массажа)'

    def __str__(self):
        return self.title


class Mountain_Body_care(models.Model):
    photo = models.ImageField(upload_to='static/photo/photo_care/', verbose_name='уходовое фото')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.CharField(max_length=250, verbose_name='описание')
    time = models.CharField(max_length=50, null=True, blank=True, verbose_name='время в формате "X/X/X"')
    price = models.CharField(max_length=50, null=False, blank=True, verbose_name='цена в формате "X/X/X"')
    popular = models.BooleanField(default=False,
                                  verbose_name='Добавить на главную страницу сайта (популярные Процедуры)')
    time_create = models.DateTimeField(verbose_name="Время создания", default=datetime.now(), )
    time_update = models.DateTimeField(verbose_name="Время изменения", default=datetime.now(), )

    class Meta:
        verbose_name_plural = 'Mountain-SPA (Уход за телом)'
        verbose_name = 'SPA-ритуалы (Уход за телом)'
        # ordering = ['-update']

    def __str__(self):
        return self.title


class Sea_SPA_RT(models.Model):
    photo = models.ImageField(upload_to='static/photo/photo_rituals/', verbose_name='уходовое фото')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.CharField(max_length=250, verbose_name='описание')
    time = models.CharField(max_length=50, null=True, blank=True, verbose_name='время в формате "X/X/X"')
    price = models.CharField(max_length=50, null=False, blank=True, verbose_name='цена в формате "X/X/X"')
    new = models.BooleanField(default=False, verbose_name='Добавить в раздел "Новые процедуры" ')
    view = models.BooleanField(default=False, verbose_name='Отображать в общем меню меню')
    time_create = models.DateTimeField(verbose_name="Время создания", default=datetime.now(), )
    time_update = models.DateTimeField(verbose_name="Время изменения", default=datetime.now(), )

    class Meta:
        verbose_name_plural = 'SEA-SPA (Виды массажа)'
        verbose_name = 'SPA-ритуалы (Вид массажа)'


class Sea_spa_BC(models.Model):
    photo = models.ImageField(upload_to='static/photo/photo_care/', verbose_name='уходовое фото')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.CharField(max_length=250, verbose_name='описание')
    time = models.CharField(max_length=50, null=True, blank=True, verbose_name='время в формате "X/X/X"')
    price = models.CharField(max_length=50, null=False, blank=True, verbose_name='цена в формате "X/X/X"')
    new = models.BooleanField(default=False, verbose_name='Добавить в раздел "Новые процедуры" ')
    view = models.BooleanField(default=True, verbose_name='Отображать в общем меню')
    time_create = models.DateTimeField(verbose_name="Время создания", default=datetime.now(), )
    time_update = models.DateTimeField(verbose_name="Время изменения", default=datetime.now(), )


    class Meta:
        verbose_name_plural = 'SEA-SPA (Уход за телом)'
        verbose_name = 'SPA-ритуалы (Уход за телом)'


class Town_SPA_RT(models.Model):
    photo = models.ImageField(upload_to='static/photo/photo_rituals/', verbose_name='уходовое фото')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.CharField(max_length=250, verbose_name='описание')
    time = models.CharField(max_length=50, null=True, blank=True, verbose_name='время в формате "X/X/X"')
    price = models.CharField(max_length=50, null=False, blank=True, verbose_name='цена в формате "X/X/X"')
    time_create = models.DateTimeField(verbose_name="Время создания", default=datetime.now(), )
    time_update = models.DateTimeField(verbose_name="Время изменения", default=datetime.now(), )

    class Meta:
        verbose_name_plural = 'Town-SPA (Виды массажа)'
        verbose_name = 'SPA-ритуалы (Вид массажа)'


class Town_spa_BC(models.Model):
    photo = models.ImageField(upload_to='static/photo/photo_care/', verbose_name='уходовое фото')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.CharField(max_length=250, verbose_name='описание')
    time = models.CharField(max_length=50, null=True, blank=True, verbose_name='время в формате "X/X/X"')
    price = models.CharField(max_length=50, null=False, blank=True, verbose_name='цена в формате "X/X/X"')
    time_create = models.DateTimeField(verbose_name="Время создания", default=datetime.now(), )
    time_update = models.DateTimeField(verbose_name="Время изменения", default=datetime.now(), )

    class Meta:
        verbose_name_plural = 'Town-SPA (Уход за телом)'
        verbose_name = 'SPA-ритуалы (Уход за телом)'


class Save_menu(models.Model):
    path = models.FileField(upload_to='static/files/',
                            verbose_name='Выберите один файл, который будет педставлять ваше Меню',
                            help_text='Это может быть только zip-файл')
    work = models.BooleanField(default=False,
                               verbose_name='Поставте галочку для того, что бы меню стало активным(возможен только один вариант!)')
    title = models.CharField(max_length=50, default=None, blank=True, null=True, verbose_name='Название Меню')
    time_create = models.DateTimeField(verbose_name="Время создания", default=datetime.now(), )
    time_update = models.DateTimeField(verbose_name="Время изменения", default=datetime.now(), )

    class Meta:
        verbose_name_plural = 'Файл меню для загрузки пользователям'
        verbose_name = 'Файл меню для загрузки пользователям'


class Plase(models.Model):
    MY_CHOICES = (
        ('KP', 'Красная Поляна'),
        ('PX', 'Роза Хутор'),
        ('GZ', 'Горно-туристический центр ПАО «Газпром»'),
    )
    MY_CHOICES = models.CharField(max_length=2, choices=MY_CHOICES,
                                  verbose_name='Расположение (выберите один из 3х варинтов)', null=True, blank=True, )
    photo = models.ImageField(upload_to='static/photo/photo_salons/', verbose_name='Фото салона', default=None)
    name = models.CharField(max_length=50, verbose_name='Имя SPA-салона', null=True, blank=True)
    adress = models.CharField(max_length=50, verbose_name='Адрес', null=True, blank=False, )
    title = models.CharField(max_length=150, verbose_name='Описание', null=True, blank=False, )
    number = models.CharField(max_length=20, verbose_name='Номер мобильного телефона', null=True, blank=True, )

    class Meta:
        verbose_name_plural = 'Расположение салонов'
        verbose_name = 'Расположения салона'
