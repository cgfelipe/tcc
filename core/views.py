from django.shortcuts import render,  get_object_or_404
from django.shortcuts import redirect
from django.template import RequestContext
from django.contrib import messages
from django.views.generic.edit import DeleteView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core import models
from tcc import forms
import uuid
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
import json


def index(request):
    return render(request, 'index.html')

#------------------ LISTA DE ITENS -----------------
def artigos(request):
    lista = models.Artigo.listar_todos()
    return render(request, 'lista_artigos.html', {"lista": lista})

def livros(request):
    lista = models.Livro.listar_todos()
    return render(request, 'lista_livros.html', {"lista": lista})

def estudantes(request):
    lista = models.Estudante.listar_todos()
    return render(request, 'estudantes.html', {"lista": lista})

def professores(request):
    lista = models.Professor.listar_todos()
    return render(request, 'lista_professores.html', {"lista": lista})

def curriculos(request):
    lista = models.Curriculo.listar_todos()
    return render(request, 'lista_curriculos.html', {"lista": lista})

def instituicoes(request):
    lista = models.Instituicao.listar_todos()
    return render(request, 'lista_instituicoes.html', {"lista": lista})

def projetos_pesquisa(request):
    lista = models.ProjetoDePesquisa.listar_todos()
    return render(request, 'lista_projetos_pesquisa.html', {"lista": lista})

def especialidades(request):
    lista = models.Especialidade.listar_todos()
    return render(request, 'lista_especialidades.html', {"lista": lista})

def departamentos(request):
    lista = models.Departamento.listar_todos()
    return render(request, 'lista_departamentos.html', {"lista": lista})

def escolaridades(request):
    lista = models.Escolaridade.listar_todos()
    return render(request, 'lista_escolaridades.html', {"lista": lista})

#------------------ CADASTRO DE ITENS -----------------
def cadastro_estudante(request):
    if request.method == 'POST':
        form = forms.EstudanteForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('listar_estudantes')
        else:
            return render(request, 'cadastro_estudante.html',
                          {'form': form})
    else:
        form = forms.EstudanteForm()
        return render(request, 'cadastro_estudante.html', {'form': form})

def cadastro_professor(request):
    if request.method == 'POST':
        form = forms.ProfessorForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('listar_professores')
        else:
            return render(request, 'cadastro_professor.html',
                          {'form': form})
    else:
        form = forms.ProfessorForm()
        return render(request, 'cadastro_professor.html', {'form': form})

def cadastro_instituicao(request):
    if request.method == 'POST':
        form = forms.InstituicaoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('listar_instituicoes')
        else:
            return render(request, 'cadastro_instituicao.html',
                          {'form': form})
    else:
        form = forms.InstituicaoForm()
        form_endereco = forms.EnderecoForm()
        return render(request, 'cadastro_instituicao.html', {'form': form, 'form_endereco': form_endereco})

def cadastro_curriculo(request):
    if request.method == 'POST':
        form = forms.CurriculoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('listar_curriculos')
        else:
            return render(request, 'cadastro_curriculo.html',
                          {'form': form})
    else:
        form = forms.CurriculoForm()
        return render(request, 'cadastro_curriculo.html', {'form': form})

def cadastro_endereco(request):
    if request.method == 'POST':
        form = forms.EnderecoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
        else:
            return render(request, 'cadastro_endereco.html',
                          {'form': form})
    else:
        form = forms.EnderecoForm()
        return render(request, 'cadastro_endereco.html', {'form': form})

def cadastro_curso(request):
    if request.method == 'POST':
        form = forms.CursoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
        else:
            return render(request, 'cadastro_curso.html',
                          {'form': form})
    else:
        form = forms.CursoForm()
        return render(request, 'cadastro_curso.html', {'form': form})

def cadastro_pessoa(request):
    if request.method == 'POST':
        form = forms.PessoaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
        else:
            return render(request, 'cadastro_pessoas.html',
                          {'form': form})
    else:
        form = forms.PessoaForm()
        return render(request, 'cadastro_pessoas.html', {'form': form})

def cadastro_escolaridade(request, form=None):
    if request.method == 'POST':
        form = forms.EscolaridadeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('listar_escolaridades.html')
    else:
        form = forms.EscolaridadeForm()
        return render(request, 'cadastro_escolaridade.html', {'form': form})

def cadastro_livro(request):
    if request.method == 'POST':
        form = forms.LivroForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('listar_livros')
        else:
            return render(request, 'cadastro_livro.html',
                          {'form': form})
    else:
        form = forms.LivroForm()
        return render(request, 'cadastro_livro.html', {'form': form})

def cadastro_projeto_pesquisa(request):
    if request.method == 'POST':
        form = forms.ProjetoPesquisaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('listar_projetos_pesquisa')
        else:
            return render(request, 'cadastro_projeto_pesquisa.html',
                          {'form': form})
    else:
        form = forms.ProjetoPesquisaForm()
        return render(request, 'cadastro_projeto_pesquisa.html', {'form': form})

def cadastro_departamento(request):
    if request.method == 'POST':
        form = forms.DepartamentoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('listar_departamentos')
        else:
            return render(request, 'cadastro_departamento.html',
                          {'form': form})
    else:
        form = forms.DepartamentoForm()
        return render(request, 'cadastro_departamento.html', {'form': form})

def cadastro_especialidade(request, form=None):
    if request.method == 'POST':
        form = forms.EspecialidadeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('listar_especialidades.html')
    else:
        form = forms.EspecialidadeForm()
        return render(request, 'cadastro_especialidade.html', {'form': form})

def cadastro_artigo(request):
    if request.method == 'POST':
        form = forms.ArtigoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('listar_artigos')
        else:
            return render(request, 'cadastro_artigo.html',
                      {'form': form})
    else:
        form = forms.ArtigoForm()
        return render(request, 'cadastro_artigo.html', {'form': form})


#------------------ EXCLUSAO DE ITENS -----------------
def excluir_especialidade(request, id):
    e = get_object_or_404(models.Especialidade, id=id)
    e.delete()
    return especialidades(request)

def excluir_escolaridade(request, id):
    e = get_object_or_404(models.Escolaridade, id=id)
    e.delete()
    return escolaridades(request)

def excluir_estudante(request, pessoa_ptr_id):
    e = get_object_or_404(models.Estudante, pessoa_ptr_id=pessoa_ptr_id)
    e.delete()
    return estudantes(request)

def excluir_professor(request, id):
    e = get_object_or_404(models.Professor, id=id)
    e.delete()
    return professores(request)

def excluir_artigo(request, id):
    e = get_object_or_404(models.Artigo, id=id)
    e.delete()
    return artigos(request)

def excluir_livro(request, id):
    e = get_object_or_404(models.Livro, id=id)
    e.delete()
    return livros(request)

def excluir_departamento(request, id):
    e = get_object_or_404(models.Departamento, id=id)
    e.delete()
    return departamentos(request)

def excluir_instituicao(request, cnpj):
    e = get_object_or_404(models.Instituicao, cnpj=cnpj)
    e.delete()
    return instituicoes(request)

def excluir_projeto_pesquisa(request, id):
    e = get_object_or_404(models.ProjetoDePesquisa, id=id)
    e.delete()
    return projetos_pesquisa(request)

def excluir_curriculo(request, id):
    e = get_object_or_404(models.Curriculo, id=id)
    e.delete()
    return curriculos(request)

#------------------ ATUALIZACAO DE ITENS --------------------------------
def atualizar_especialidade(request, id):
    e = get_object_or_404(models.Especialidade, id=id)
    if request.method == 'POST':
        form = forms.EspecialidadeForm(request.POST, instance=e)
        if form.is_valid():
            form.save()
            return especialidades(request)
    else:
        form = forms.EspecialidadeForm(instance=e)
        return render(request, 'atualizar_especialidade.html', {'form': form, 'obj': e})


def atualizar_escolaridade(request, id):
    e = get_object_or_404(models.Escolaridade, id=id)
    if request.method == 'POST':
        form = forms.EscolaridadeForm(request.POST, instance=e)
        if form.is_valid():
            form.save()
            return escolaridades(request)
    else:
        form = forms.EscolaridadeForm(instance=e)
        return render(request, 'atualizar_escolaridade.html', {'form': form, 'obj': e})

def atualizar_estudante(request, id):
    e = get_object_or_404(models.Estudante, id=id)
    if request.method == 'POST':
        form = forms.EstudanteForm(request.POST, instance=e)
        if form.is_valid() and form:
            form.save()
            return estudantes(request)
    else:
        form = forms.EstudanteForm(instance=e)
        return render(request, 'atualizar_estudante.html', {'form': form, 'obj': e})

def atualizar_professor(request, id):
    e = get_object_or_404(models.Professor, id=id)
    if request.method == 'POST':
        form = forms.ProfessorForm(request.POST, instance=e)
        if form.is_valid() and form:
            form.save()
            return professores(request)
    else:
        form = forms.ProfessorForm(instance=e)
        print(form)
        print(request)
        return render(request, 'atualizar_professor.html', {'form': form, 'obj': e})

def atualizar_artigo(request, id):
    e = get_object_or_404(models.Artigo, id=id)
    if request.method == 'POST':
        form = forms.ArtigoForm(request.POST, instance=e)
        if form.is_valid() and form:
            form.save()
            return artigos(request)
    else:
        form = forms.ArtigoForm(instance=e)
        return render(request, 'atualizar_artigo.html', {'form': form, 'obj': e})

def atualizar_livro(request, id):
    e = get_object_or_404(models.Livro, id=id)
    if request.method == 'POST':
        form = forms.LivroForm(request.POST, instance=e)
        if form.is_valid() and form:
            form.save()
            return livros(request)
    else:
        form = forms.LivroForm(instance=e)
        return render(request, 'atualizar_livro.html', {'form': form, 'obj': e})

def atualizar_departamento(request, id):
    e = get_object_or_404(models.Departamento, id=id)
    if request.method == 'POST':
        form = forms.DepartamentoForm(request.POST, instance=e)
        if form.is_valid():
            form.save()
            return departamentos(request)
    else:
        form = forms.DepartamentoForm(instance=e)
        return render(request, 'atualizar_departamento.html', {'form': form, 'obj': e})

def atualizar_instituicao(request, cnpj):
    e = get_object_or_404(models.Instituicao, cnpj=cnpj)
    if request.method == 'POST':
        form = forms.InstituicaoForm(request.POST, instance=e)
        if form.is_valid():
            form.save()
            return instituicoes(request)
    else:
        form = forms.InstituicaoForm(instance=e)
        return render(request, 'atualizar_instituicao.html', {'form': form, 'obj': e})

def atualizar_projeto_pesquisa(request, id):
    e = get_object_or_404(models.ProjetoDePesquisa, id=id)
    if request.method == 'POST':
        form = forms.ProjetoPesquisaForm(request.POST, instance=e)
        if form.is_valid():
            form.save()
            return projetos_pesquisa(request)
    else:
        form = forms.ProjetoPesquisaForm(instance=e)
        return render(request, 'atualizar_projeto_pesquisa.html', {'form': form, 'obj': e})

def atualizar_curriculo(request, id):
    e = get_object_or_404(models.Curriculo, id=id)
    if request.method == 'POST':
        form = forms.CurriculoForm(request.POST, instance=e)
        if form.is_valid():
            form.save()
            return curriculos(request)
    else:
        form = forms.CurriculoForm(instance=e)
        return render(request, 'atualizar_curriculo.html', {'form': form, 'obj': e})