from django.contrib import admin
from django.urls import path
from projetoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('brecho/clientes', views.listar_clientes, name='listar_clientes'),
    path('brecho/roupas', views.listar_roupas, name='listar_roupas'),
]
