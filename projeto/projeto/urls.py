from django.contrib import admin
from django.urls import path
from projetoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('clientes/', views.cliente, name='listarclientes'),
    path('roupas/', views.roupa, name='listagemroupas'),
]
