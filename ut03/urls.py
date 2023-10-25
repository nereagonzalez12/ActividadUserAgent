from django.urls import path

from ut03 import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('crea_tablero/', views.crea_tablero, name='crea_tablero'),
]