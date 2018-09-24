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
    return render(request, 'list_projetos_pesquisa.html')


def departamentos(request):
    return render(request, 'list_departamentos.html')


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
