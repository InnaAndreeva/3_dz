from django.urls import path

from . import views

urlpatterns = [
    path('', views.apply_for_study, name='apply_for_study'),
    path('send_application', views.send_application, name='send_application'),
]
