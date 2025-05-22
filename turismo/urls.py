from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicioSite, name='inicio'),
    path('sucesso/', views.pagina_de_sucesso, name='pagina_de_sucesso'),

]

