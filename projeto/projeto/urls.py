from django.contrib import admin
from django.urls import path
from projetoapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('opcaoclientes/', views.opcoesclientes, name='opcoescli'),
    path('opcaoroupas/', views.opcoesroupas, name='opcoesrou'),
    path('opcoesvendas/', views.opcoesvendas, name='opcoesven'),

    path('cliente/', views.criar_cliente, name='criar_cliente'),
    path('cliente/excluir/', views.excluir_cliente, name='excluir_cliente'),
    path('cliente/atualizar/', views.atualizar_cliente, name='atualizar_cliente'),

    path('roupa/', views.criar_roupa, name='criar_roupa'),
    path('roupa/excluir/', views.excluir_roupa, name='excluir_roupa'),
    path('roupa/atualizar/', views.atualizar_roupa, name='atualizar_roupa'),

    path('venda/', views.criar_venda, name='criar_venda'),
    path('venda/excluir/', views.excluir_venda, name='excluir_venda'),
    path('venda/atualizar/', views.atualizar_venda, name='atualizar_venda'),
] + static(settings.MEDIA_URL, document_ROOT=settings.MEDIA_ROOT)