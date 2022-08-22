"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('news', views.news, name='news'),
    path('calendrier', views.calendrier, name='calendrier'),
    path('machines', views.machines, name='machines'),
    path('tarifs', views.tarifs, name='tarifs'),
    path('adhesion', views.adhesion, name='adhesion'),
    path('galerie', views.galerie, name='galerie'),
    path('about', views.about, name='about'),
    path('utilisateur', views.utilisateur, name='utilisateur'),
    path('edit_utilisateur', views.edit_utilisateur, name='edit_utilisateur'),
    
    path('calendar', views.CalendarView.as_view(), name='calendar'),
]
