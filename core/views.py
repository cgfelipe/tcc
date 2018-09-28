from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import Estudante
from tcc import forms
import uuid
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


def index(request):
    return render(request, 'index.html')


def artigos(request):
    return render(request, 'lista_artigos.html')


def livros(request):
    return render(request, 'lista_livros.html')


def estudantes(request):
    return render(request, 'estudantes.html')


def curriculos(request):
    return render(request, 'lista_curriculos.html')


def instituicoes(request):
    return render(request, 'lista_instituicoes.html')


def projetos_pesquisa(request):
    return render(request, 'lista_projetos_pesquisa.html')


def departamentos(request):
    return render(request, 'lista_departamentos.html')

def cadastro_estudante(request):
    if request.method == 'POST':
        form = forms.EstudanteForm(request.POST)
        form_endereco = forms.EnderecoForm(request.POST)
        if form.is_valid() & form_endereco.is_valid():
            post = form.save(commit=False)
            post.save()
            post_endereco = form_endereco.save(commit=False)
            post_endereco.save()
            return redirect('estudantes.html')
    else:
        form = forms.EstudanteForm()
        form_endereco = forms.EnderecoForm()
        return render(request, 'cadastro_estudante.html', {'form': form, 'form_endereco': form_endereco})

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

def cadastro_especialidade(request):
    if request.method == 'POST':
        form = forms.EspecialidadeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = forms.EspecialidadeForm()
    return render(request, 'cadastro_especialidade.html', {'form': form})


def cadastro_escolaridade(request):
    if request.method == 'POST':
        form = forms.EscolaridadeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
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



@api_view(['POST'])
@csrf_exempt
def registrar_estudante(request):
    Estudante(**request.data).save()
    return Response(status=200)


@api_view(['GET'])
def listar_estudantes(request):
    return Response(json.dumps(Estudante.listar_todos()), status=200)


@api_view(['POST'])
def atualizar_estudante(request):
    e = Estudante.buscar(cpf=request.data['cpf'])
    update_dict = dict(request.data)
    del update_dict['cpf']
    e.atualizar(**update_dict)
    return Response(status=200)


@api_view(['DELETE'])
def remover_estudante(request):
    e = Estudante.buscar(cpf=request.data['cpf'])
    e.remover()
    return Response(status=200)
