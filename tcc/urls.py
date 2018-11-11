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

    url(r'^cadastro_pessoa', entities_views.cadastro_pessoa,
        name='cadastro_pessoa'),
    url(r'^cadastro_endereco', entities_views.cadastro_endereco,
        name='cadastro_endereco'),

    url(r'^listar_estudante', entities_views.estudantes, name='listar_estudantes'),
    url(r'^cadastro_estudante', entities_views.cadastro_estudante,
        name='cadastro_estudante'),
    url(r'^excluir_estudante/(?P<id>\d+)$', entities_views.excluir_estudante,
        name='excluir_estudante'),
    url(r'^atualizar_estudante/(?P<id>\d+)$', entities_views.atualizar_estudante,
        name='atualizar_estudante'),


    url(r'^listar_professores', entities_views.professores, name='listar_professores'),
    url(r'^cadastro_professor', entities_views.cadastro_professor,
        name='cadastro_professor'),
    url(r'^excluir_professor/(?P<id>\d+)$', entities_views.excluir_professor,
        name='excluir_professor'),
    url(r'^atualizar_professor/(?P<id>\d+)$', entities_views.atualizar_professor,
        name='atualizar_professor'),


    url(r'^listar_artigos', entities_views.artigos, name='listar_artigos'),
    url(r'^cadastro_artigo', entities_views.cadastro_artigo,
        name='cadastro_artigo'),
    url(r'^excluir_artigo/(?P<id>\d+)$', entities_views.excluir_artigo,
        name='excluir_artigo'),
    url(r'^atualizar_artigo/(?P<id>\d+)$', entities_views.atualizar_artigo,
        name='atualizar_artigo'),


    url(r'^listar_livros', entities_views.livros, name='listar_livros'),
    url(r'^cadastro_livro', entities_views.cadastro_livro,
        name='cadastro_livro'),
    url(r'^excluir_livro/(?P<id>\d+)$', entities_views.excluir_livro,
        name='excluir_livro'),
    url(r'^atualizar_livro/(?P<id>\d+)$', entities_views.atualizar_livro,
        name='atualizar_livro'),


    url(r'^listar_curriculos', entities_views.curriculos,  name='listar_curriculos'),
    url(r'^cadastro_curriculo', entities_views.cadastro_curriculo, name='cadastro_curriculo'),
    url(r'^excluir_curriculo/(?P<id>\d+)$', entities_views.excluir_curriculo,
        name='excluir_curriculo'),
    url(r'^atualizar_curriculo/(?P<id>\d+)$', entities_views.atualizar_curriculo,
        name='atualizar_curriculo'),


    url(r'^listar_instituicoes', entities_views.instituicoes,
        name='listar_instituicoes'),
    url(r'^cadastro_instituicao', entities_views.cadastro_instituicao,
        name='cadastro_instituicao'),
    url(r'^excluir_instituicao/(?P<id>\d+)$', entities_views.excluir_instituicao,
        name='excluir_instituicao'),
    url(r'^atualizar_instituicao/(?P<id>\d+)$', entities_views.atualizar_instituicao,
        name='atualizar_instituicao'),


    url(r'^listar_projetos_pesquisa', entities_views.projetos_pesquisa,
        name='listar_projetos_pesquisa'),
    url(r'^cadastro_projeto_pesquisa', entities_views.cadastro_projeto_pesquisa,
        name='cadastro_projeto_pesquisa'),
    url(r'^excluir_projeto_pesquisa', entities_views.excluir_projeto_pesquisa,
        name='excluir_projeto_pesquisa'),


    url(r'^listar_departamentos', entities_views.departamentos,
        name='listar_departamentos'),
    url(r'^cadastro_departamento', entities_views.cadastro_departamento,
        name='cadastro_departamento'),
    url(r'^excluir_departamento/(?P<id>\d+)$', entities_views.excluir_departamento,
        name='excluir_departamento'),
    url(r'^atualizar_departamento/(?P<id>\d+)$', entities_views.atualizar_departamento,
        name='atualizar_departamento'),


    url(r'^listar_especialidades', entities_views.especialidades,
        name='listar_especialidades'),
    url(r'^cadastro_especialidade', entities_views.cadastro_especialidade,
        name='cadastro_especialidade'),
    url(r'^excluir_especialidade/(?P<id>\d+)$', entities_views.excluir_especialidade,
        name='excluir_especialidade'),
    url(r'^atualizar_especialidade/(?P<id>\d+)$', entities_views.atualizar_especialidade,
        name='atualizar_especialidade'),


    url(r'^listar_escolaridades', entities_views.escolaridades,
        name='listar_escolaridades'),
    url(r'^cadastro_escolaridade', entities_views.cadastro_escolaridade,
        name='cadastro_escolaridade'),
    url(r'^excluir_escolaridade', entities_views.excluir_escolaridade,
        name='excluir_escolaridade'),


    url(r'$', admin.site.login, name='login_gui'),
]
