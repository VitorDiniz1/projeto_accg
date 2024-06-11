"""
URL configuration for projeto_accg project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from app.views import home, adminAccg, cadastro, create, animal, editar, atualizar, deletar, help, contato, filtro, paginaAnimal, loginAdmin, dologin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('admin-accg/', adminAccg, name='adminAccg'),
    path('admin-accg/cadastrar/', cadastro, name='cadastro'),
    path('admin-accg/animal/<int:pk>/', animal, name='animal'),
    path('admin-accg/editar/<int:pk>/', editar, name='editar'),
    path('admin-accg/atualizar/<int:pk>/', atualizar, name='atualizar'),
    path('admin-accg/deletar/<int:pk>/', deletar, name='deletar'),
    path('admin-accg/create/', create),
    path('help/', help),
    path('contato/', contato),
    path('filtro/', filtro, name='filtro'),
    path('paginaAnimal/<int:pk>/', paginaAnimal, name='paginaAnimal'),
    path('login/', loginAdmin, name='login'),
    path('dologin/', dologin),
]
