from core.modelos.repositorios.base_repositorio import BaseRepositorio
from core.modelos.entidades.Endereco import Endereco


class RepositorioEndereco(BaseRepositorio):
    def cadastrar(self, endereco: Endereco):
        return endereco.save()

    def buscar(self, cep, numero):
        return Endereco.objects.get(cep=cep, numero=numero)

    def listar_todos(self):
        return Endereco.objects.all()

    def atualizar(self, cep, numero, **kwargs):
        modifiers = dict(**kwargs)
        for k, v in kwargs.items():
            if not hasattr(Endereco, k):
                del modifiers[k]
        endereco = Endereco.objects.filter(cep=cep, numero=numero)
        endereco.update(**modifiers)
        return endereco.first()

    def remover(self, **kwargs):
        endereco = Endereco.objects.get(**kwargs)
        if endereco:
            endereco.delete()
