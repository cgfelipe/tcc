"""tcc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.contrib import admin
from django.conf.urls import (
    url, include
)
from django.contrib import admin
from rest_framework import routers
from core import views as entities_views
from django.views.decorators.csrf import csrf_exempt

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^admin', entities_views.index, name='index'),
    url(r'^listar_estudante', entities_views.estudantes, name='listar_estudantes'),
    url(r'^listar_artigos', entities_views.artigos, name='listar_artigos'),
    url(r'^listar_livros', entities_views.livros, name='listar_livros'),
    url(r'^listar_curriculos', entities_views.curriculos,  name='listar_curriculos'),
    url(r'^listar_instituicoes', entities_views.instituicoes,
        name='listar_instituicoes'),
    url(r'^listar_projetos_pesquisa', entities_views.projetos_pesquisa,
        name='listar_projetos_pesquisa'),
    url(r'^listar_departamentos', entities_views.departamentos,
        name='listar_departamentos'),
    url(r'$', admin.site.login, name='login_gui'),
]
