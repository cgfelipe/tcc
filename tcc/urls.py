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
    # path('/admin', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^cadastrar_estudante', csrf_exempt(entities_views.registrar_estudante), name='registrar_estudante'),
    url(r'$', admin.site.login, name='login_gui'),
    # path('/listar_estudantes', views.listar_estudantes),
    # path('/cadastrar_professor', views.cadastrar_professor),
    # path('/listar_professores', views.listar_professores),
    # path('/cadastrar_departamento', views.cadastrar_departamento),
    # path('/listar_departamentos', views.listar_departamentos),
    # path('/cadastrar_instituicao', views.cadastrar_instituicao),
    # path('/listar_instituicoes', views.listar_instituicoes),
    # path('/cadastrar_livro', views.cadastrar_livro),
    # path('/listar_livros', views.listar_livros),
    # path('/cadastrar_curriculo', views.cadastrar_curriculo),
    # path('/listar_curriculos', views.listar_curriculos),
    # path('/cadastrar_projeto_pesquisa', views.cadastrar_projeto_pesquisa),
    # path('/listar_projetos_pesquisa', views.listar_projetos_pesquisa),
    # path('/cadastrar_especialidade', views.cadastrar_especialidade),
    # path('/listar_especialidades', views.listar_especialidades),
]
