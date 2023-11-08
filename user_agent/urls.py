from django.urls import path

from . import views

urlpatterns = [
    path('', views.first_view, name='first-view'),
    path('info/', views.info_view, name='info-view'),
    path('dispositivos/', views.dispositivos_view, name='dispositivos-view'),
]
