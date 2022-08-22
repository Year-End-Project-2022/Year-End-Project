from django.urls import path
from . import views
from django.urls import path


urlpatterns = [
    path('ateliers', views.ateliers, name='ateliers'),
    path('atelier/<str:name>', views.atelier, name='atelier'),
    path('atelier/<str:name>/interested', views.interested, name="interested"),
]