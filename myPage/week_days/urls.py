from django.urls import path
from . import views


urlpatterns = [
    path('<week_days>/', views.get_info_about_week_days),
    # path('monday/', views.monday),
    # path('tuesday/', views.tuesday),




]
