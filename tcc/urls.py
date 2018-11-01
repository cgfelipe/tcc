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
    url(r'^listar_especialidades', entities_views.especialidades,
        name='listar_especialidades'),
    url(r'^listar_escolaridades', entities_views.escolaridades,
        name='listar_escolaridades'),
    url(r'^cadastro_especialidade', entities_views.cadastro_especialidade,
        name='cadastro_especialidade'),
    url(r'^cadastro_estudante', entities_views.cadastro_estudante,
        name='cadastro_estudante'),
    url(r'^cadastro_professor', entities_views.cadastro_professor,
        name='cadastro_professor'),
    url(r'^cadastro_escolaridade', entities_views.cadastro_escolaridade,
        name='cadastro_escolaridade'),
    url(r'^cadastro_livro', entities_views.cadastro_livro,
        name='cadastro_livro'),
    url(r'^cadastro_curriculo', entities_views.cadastro_curriculo,
        name='cadastro_curriculo'),
    url(r'^cadastro_instituicao', entities_views.cadastro_instituicao,
        name='cadastro_instituicao'),
    url(r'^cadastro_artigo', entities_views.cadastro_artigo,
        name='cadastro_artigo'),
    url(r'^cadastro_projeto_pesquisa', entities_views.cadastro_projeto_pesquisa,
        name='cadastro_projeto_pesquisa'),
    url(r'^cadastro_departamento', entities_views.cadastro_departamento,
        name='cadastro_departamento'),
    url(r'^cadastro_especialidade', entities_views.cadastro_especialidade,
        name='cadastro_especialidade'),
    url(r'^excluir_escolaridade', entities_views.excluir_escolaridade,
        name='excluir_escolaridade'),
    url(r'^excluir_especialidade/(?P<id>\d+)$', entities_views.excluir_especialidade,
        name='excluir_especialidade'),
    url(r'^atualizar_especialidade/(?P<id>\d*)$', entities_views.atualizar_especialidade,
        name='atualizar_especialidade'),
    url(r'$', admin.site.login, name='login_gui'),
]
