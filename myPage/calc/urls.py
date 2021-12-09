from django.urls import path
from . import views

urlpatterns = [
    path('<int:width>*<int:height>', views.get_square)



]