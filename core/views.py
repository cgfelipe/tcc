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

# Create your views here.


def index(request):
    return render(request, 'index.html')
#
# class EspecialidadeDelete(DeleteView):
#     print(DeleteView)
#     model = models.Especialidade.remover()
#     success_url = reverse_lazy('lista_especialidades')


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
    print(lista)
    return render(request, 'lista_escolaridades.html', {"lista": lista})


def cadastro_estudante(request):
    if request.method == 'POST':
        form = forms.EstudanteForm(request.POST)
        form_pessoa= forms.PessoaForm(request.POST)
        print(form_pessoa.errors)
        if form.is_valid() & form_pessoa.is_valid():
            # post_endereco = form_endereco.save(commit=False)
            # post_endereco.save()
            post_pessoa = form_pessoa.save(commit=False)
            post_pessoa.save()
            post = form.save(commit=False)
            post.save()
            return render(request, 'estudantes.html')
        else:
            return render(request, 'cadastro_estudante.html',
                          {'form': form, 'form_pessoa': form_pessoa})
    else:
        form = forms.EstudanteForm()
        # form_endereco = forms.EnderecoForm()
        form_pessoa = forms.PessoaForm()
        return render(request, 'cadastro_estudante.html', {'form': form, 'form_pessoa': form_pessoa})


def cadastro_professor(request):
    if request.method == 'POST':
        form = forms.ProfessorForm(request.POST)
        form_endereco = forms.EnderecoForm(request.POST)
        form_pessoa = forms.PessoaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            post_endereco = form_endereco.save(commit=False)
            post_endereco.save()
            post_pessoa = form_pessoa.save(commit=False)
            post_pessoa.save()
            return redirect('lista_professores.html')
    else:
        form_pessoa = forms.PessoaForm()
        form_endereco = forms.EnderecoForm()
        form = forms.ProfessorForm()
        return render(request, 'cadastro_professor.html', {'form': form, 'form_endereco': form_endereco, 'form_pessoa': form_pessoa})




def cadastro_instituicao(request):
    if request.method == 'POST':
        form = forms.InstituicaoForm(request.POST)
        form_endereco = forms.EnderecoForm(request.POST)
        if form.is_valid() & form_endereco.is_valid():
            post = form.save(commit=False)
            post.save()
            post_endereco = form_endereco.save(commit=False)
            post_endereco.save()
            return redirect('lista_instituicoes.html')
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
            return redirect('lista_curriculos.html')
    else:
        form = forms.LivroForm()
        return render(request, 'cadastro_curriculo.html', {'form': form})

def cadastro_endereco(request):
    if request.method == 'POST':
        form = forms.EnderecoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index.html')
    else:
        form = forms.EnderecoForm()
        return render(request, 'cadastro_endereco.html', {'form': form})

def cadastro_pessoa(request):
    if request.method == 'POST':
        form = forms.PessoaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index.html')
    else:
        form = forms.PessoaForm()
        return render(request, 'cadastro_pessoas.html', {'form': form})

def cadastro_escolaridade(request):
    if request.method == 'POST':
        form = forms.EscolaridadeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('lista_escolaridade.html')
    else:
        form = forms.EspecialidadeForm()
    return render(request, 'cadastro_escolaridade.html', {'form': form})


def cadastro_livro(request):
    if request.method == 'POST':
        form = forms.LivroForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('lista_livros.html')
    else:
        form = forms.LivroForm()
        return render(request, 'cadastro_livro.html', {'form': form})


def cadastro_projeto_pesquisa(request):
    if request.method == 'POST':
        form = forms.ProjetoPesquisaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('lista_projetos_pesquisa.html')
    else:
        form = forms.ProjetoPesquisaForm()
        return render(request, 'cadastro_livro.html', {'form': form})


def cadastro_departamento(request):
    if request.method == 'POST':
        form = forms.DepartamentoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('lista_departamentos.html')
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
            return redirect('lista_artigos.html')
    else:
        form = forms.ArtigoForm()
        return render(request, 'cadastro_artigo.html', {'form': form})

def excluir_escolaridade(request):
    if request.method == 'DELETE':
        models.Escolaridade.remover()
        return redirect(request, 'lista_escolaridades.html')

#------------------ AQUI FUNCIONANDO -----------------
def excluir_especialidade(request, id):
    e = get_object_or_404(models.Especialidade, id=id)
    e.delete()
    return especialidades(request)
#------------------------------------------------------

def excluir_estudante(request, id):
    e = get_object_or_404(models.Estudante, id=id)
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

#------------------ AQUI FUNCIONANDO --------------------------------
def atualizar_especialidade(request, id):
    e = get_object_or_404(models.Especialidade, id=id)
    if request.method == 'POST':
        form = forms.EspecialidadeForm(request.POST, instance=e)
        if form.is_valid():
            form.save()
            return especialidades(request)
    else:
        form = forms.EspecialidadeForm(instance=e)
        print(form)
        print(request)
        return render(request, 'atualizar_especialidade.html', {'form': form, 'obj': e})
#---------------------------------------------------------------------------------------

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
        form = forms.ProfessorForm(request.POST, instance=e)
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