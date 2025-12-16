from django.contrib import admin
from django.urls import include, path

# Импортируем информацию из настроек
from django.conf import settings

urlpatterns = [
    path('', include('homepage.urls')),
    path('about/', include('about.urls')),
    path('ice_cream/', include('ice_cream.urls')),
    path('admin/', admin.site.urls),
]
