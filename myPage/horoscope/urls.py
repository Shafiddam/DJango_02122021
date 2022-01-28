from django.urls import path
from . import views

#                                ________________horoscope_urls___________________
urlpatterns = [
    path('', views.index),
    path('Типы_стихий/', views.type),
    path('Типы_стихий/Огонь', views.type_Fire),
    path('Типы_стихий/Земля', views.type_Earth),
    path('Типы_стихий/Воздух', views.type_Air),
    path('Типы_стихий/Вода', views.type_Water),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope-name'),
    path('<int:day>/<int:month>', views.get_sign_zodiac),




]
