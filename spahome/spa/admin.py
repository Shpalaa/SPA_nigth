from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

admin.site.site_title = 'Админ-панель SPA-салонов'
admin.site.site_header = 'Админ-панель SPA-салонов'


# admin.site.register('Rituals')

@admin.register(Rituals)
class RitualsAdmin(admin.ModelAdmin):
    list_display = ("title", "popular",)
    fields = ('photo', 'title', 'content', 'time', 'price', 'popular', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update')


@admin.register(Body_care)
class Body_careAdmin(admin.ModelAdmin):
    list_display = ("title", "popular",)


@admin.register(Sea_SPA_RT)
class Sea_SPA_RTAdmin(admin.ModelAdmin):
    list_display = ("title", "popular",)


@admin.register(Sea_spa_BC)
class Sea_spa_BCAdmin(admin.ModelAdmin):
    list_display = ("title", "popular",)


@admin.register(Save_menu)
class Save_menuAdmin(admin.ModelAdmin):
    list_display = ('title', 'work',)


@admin.register(Plase)
class PlaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'MY_CHOICES',)
