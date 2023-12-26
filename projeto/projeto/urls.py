from django.contrib import admin
from django.urls import path
from projetoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
    path('opcaoclientes/', views.opcoescli, name='opcaocli'),
    path('opcaoroupas/', views.opcoesrou, name='opcoesrou'),

    path('cliente/', views.criar_cliente, name='criar_cliente'),
    path('cliente/excluircliente', views.excluir_cliente, name='excluir_cliente'),

    path('roupa/', views.criar_roupa, name='criar_roupa'),
    path('roupa/excluirroupa', views.excluir_roupa, name='excluir_roupa'),

    path('listagem/', views.listartudo, name='listartudo'),
]
