from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import Estudante
import uuid
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@api_view(['POST'])
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