from django.urls import path, include
from django.contrib.auth.views import LoginView
from .views import applications_by_status, edit_application
from . import views

app_name = 'head_admin'

urlpatterns = [
    path('', views.applications_by_status, name='applications_by_status'),
    path('<int:application_id>/edit', views.edit_application, name='edit_application'),
    path('<int:application_id>/archive', views.archive_application, name='archive_application'),

]
