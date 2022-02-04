from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('VS_Code', views.VS_Code),
    path('PyCharm', views.PyCharm),
    path('VS_Code', views.VS_Code),
    path('Панель администратора', admin.site.urls),



]
