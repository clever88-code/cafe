from django.urls import path, include
from django.contrib.auth.views import LoginView
from .views import lab_cabinet_applications, take_application,change_application
from . import views

app_name = "labs_applications"

urlpatterns = [
    path('', views.lab_cabinet_applications, name='lab_cabinet_applications'),
    path('<int:application_id>/take', views.take_application, name='take_application'),
    path('<int:application_id>/change', views.change_application, name='change_application'),
    

]
