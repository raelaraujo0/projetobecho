from django.contrib import admin
from django.urls import path
from projetoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    ## HOME -> OPCOES

    path('opcaoclientes/', views.opcoescli, name='opcaocli'),
    path('opcaoroupas/', views.opcoesrou, name='opcoesrou'),
    ## OPCOES -> CLIENTE/ROUPAS

    ## CLIENTES
    path('cliente/', views.criar_cliente, name='criar_cliente'),
    path('cliente/excluir/', views.excluir_cliente, name='excluir_cliente'),
    path('cliente/atualizar/', views.atualizar_cliente, name='atualizar_cliente'),

    ## ROUPAS
    path('roupa/', views.criar_roupa, name='criar_roupa'),
    path('roupa/excluir/', views.excluir_roupa, name='excluir_roupa'),
    path('roupa/atualizar/', views.atualizar_roupa, name='atualizar_roupa'),

    path('listagem/', views.listartudo, name='listartudo'),
]
