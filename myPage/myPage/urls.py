from django.contrib import admin
from django.urls import path, include
from . import views

url1 = 'admin/'
url2 = 'horoscope/'
url3 = 'week_days/'
url4 = 'calc/'
# url5 = 'horoscope/type'

urlpatterns = [
    path('', views.index),
    path(url1, admin.site.urls),
    path(url2, include('horoscope.urls')),
    path(url3, include('week_days.urls')),
    path(url4, include('calc.urls')),
    # path(url5, include('horoscope.urls')),

]
