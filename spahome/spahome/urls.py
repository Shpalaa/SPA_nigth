from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
import debug_toolbar
from spa.views import index

urlpatterns = [
    path('', index, name='index'),
    path('home/', include('spa.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),

]
