from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('Прямоугольник/<int:width>/<int:height>', views.get_rectangle_area),
    path('Прямоугольник', views.rectangle_area),
    # path('Квадрат/<int:width>', views.square_area),
    path('Квадрат', views.square_area),
    # path('Круг/<int:radius>', views.circle_area),
    path('Круг', views.circle_area),



]





