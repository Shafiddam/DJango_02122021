from django.urls import path
from . import views

#                                ________________horoscope_urls___________________
urlpatterns = [
    path('', views.index),
    path('type/', views.type),
    path('type/Fire', views.type_Fire),
    path('type/Earth', views.type_Earth),
    path('type/Air', views.type_Air),
    path('type/Water', views.type_Water),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope-name'),
    path('<int:day>/<int:month>', views.get_sign_zodiac),




]
