from django.contrib import admin
from django.urls import path
from projetoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('clientes', views.criar_cliente, name='criar_cliente'),
    path('roupas', views.criar_roupa, name='criar_roupa'),
    path('listagem/', views.listartudo, name='listartudo'),
]