from django.urls import path
from . import views

# Гороскоп_урлс
urlpatterns = [
    path('', views.index),
    path('type/', views.type),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope-name'),
    path('<type_zodiac>/', views.get_info_about_type_zodiac, name='horoscope-type'),


    # path('skorpio/', views.skorpio),
    # path('virgo/', views.virgo),
    # path('aries/', views.aries),
    # path('sagittarius/', views.sagittarius),
    # path('taurus/', views.taurus),

]
