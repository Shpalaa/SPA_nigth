from django.urls import path
from django.conf.urls.static import static
from .views import *
# from google import views as view

urlpatterns = [
    path('', home, name='home'),
    path('spa_menu/', spa_menu, name='spa_menu'),
    path('about_us/', about_us, name='about_us'),
    path('masters/', masters, name='masters'),
    path('qualifications/', qualifications, name='qualifications'),
    path('salons/', salons, name='salons'),
    path('contacts/', contacts, name='contacts'),
    path('certificate/', certificate, name='certificate'),
    path('Mountain_SPA/', Mountain_SPA, name='Mountain_spa'),
    path('Sea_SPA/', Sea_SPA, name='Sea_spa'),

    # path('maps/', maps, name='maps'),

]
