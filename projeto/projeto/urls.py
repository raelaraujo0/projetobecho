from django.contrib import admin
from django.urls import path
from projetoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    ## HOME -> OPCOES

    path('opcaoclientes/', views.opcoescli, name='opcaocli'),
    path('opcaoroupas/', views.opcoesrou, name='opcoesrou'),
    path('opcoesvendas/', views.opcoesven, name='opcoesven'),
    ## OPCOES -> CLIENTE/ROUPAS

    ## CLIENTES
    path('cliente/', views.criar_cliente, name='criar_cliente'),
    path('cliente/excluir/<int:idcliente>/', views.excluir_cliente, name='excluir_cliente'),
    path('cliente/atualizar/<int:idcliente>/', views.atualizar_cliente, name='atualizar_cliente'),

    ## ROUPAS
    path('roupa/', views.criar_roupa, name='criar_roupa'),
    path('roupa/excluir/<int:idroupa>/', views.excluir_roupa, name='excluir_roupa'),
    path('roupa/atualizar/<int:idroupa>/', views.atualizar_roupa, name='atualizar_roupa'),

    ## VENDAS
    path('venda/', views.criar_venda, name='criar_venda'),
    path('venda/excluir/<int:idvenda>/', views.excluir_venda, name='excluir_venda'),
    path('venda/atualizar/<int:idvenda>/', views.atualizar_venda, name='atualizar_venda'),

    path('listagem/', views.listartudo, name='listartudo'),
]
