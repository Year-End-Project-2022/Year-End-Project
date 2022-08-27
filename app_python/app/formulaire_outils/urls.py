from django.urls import path
from . import views

urlpatterns = [
    #path('', views.listview, name='outil_list_view'),
    path('<str:id>/', views.outil_render_pdf_view, name='outil_pdf_view'),
]