from django.contrib import admin
from django.urls import path, include
from . import views

url1 = 'Admin'
url2 = 'Гороскоп/'
url3 = 'Ежедневник/'
url4 = 'Калькулятор/'
url5 = 'Типы_стихий/'
url6 = 'Площадь_фигур/'

urlpatterns = [
    path('', views.index),
    path(url1, admin.site.urls),
    path(url2, include('horoscope.urls')),
    path(url3, include('week_days.urls')),
    path(url4, include('calc.urls')),
    path(url5, include('horoscope.urls')),
    path(url6, include('geometry.urls')),

]
