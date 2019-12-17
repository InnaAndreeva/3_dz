from django.urls import path

from . import views

urlpatterns = [
    # path('', views.sports, name='sport_sections'),
    path('', views.show_sports, name='show_sports'),
    path('sport_sections/<int:sport_id>', views.show_sport_sections_by_sport, name='show_sport_sections_by_sport'),
]
