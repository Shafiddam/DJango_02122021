from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('Прямоугольник/<int:width>/<int:height>', views.get_rectangle_area),
    path('Квадрат/<int:width>', views.get_square_area),
    path('Круг/<int:radius>', views.get_circle_area),



]


