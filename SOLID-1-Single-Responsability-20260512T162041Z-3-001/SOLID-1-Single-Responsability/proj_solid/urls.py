"""
URL configuration for proj_bd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from app import views

urlpatterns = [
    path('', views.HomeView.home, name='home'),

    path('categorias/', views.CategoriasView.categorias_listar, name='categorias'),
    path('categorias/incluir/', views.CategoriasView.categorias_incluir, name='categorias_incluir'),
    path('categorias/alterar/<int:id>/', views.CategoriasView.categorias_alterar, name='categorias_alterar'),
    path('categorias/excluir/<int:id>/', views.CategoriasView.categorias_excluir, name='categorias_excluir'),
    path('categorias/salvar/', views.CategoriasView.categorias_salvar, name='categorias_salvar'),

    path('produtos/', views.ProdutosView.produtos_listar, name='produtos'),
    path('produtos/incluir/', views.ProdutosView.produtos_incluir, name='produtos_incluir'),
    path('produtos/alterar/<int:id>/', views.ProdutosView.produtos_alterar, name='produtos_alterar'),
    path('produtos/excluir/<int:id>/', views.ProdutosView.produtos_excluir, name='produtos_excluir'),
    path('produtos/salvar/', views.ProdutosView.produtos_salvar, name='produtos_salvar'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
