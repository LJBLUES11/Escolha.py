from django.urls import path

from . import views

urlpatterns = [
    path('', views.jogo_view, name='jogo'),
    path('reiniciar/', views.reiniciar, name='reiniciar'),
]
