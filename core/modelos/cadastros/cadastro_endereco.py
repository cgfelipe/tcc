from core.modelos.repositorios.base_repositorio import BaseRepositorio


class CadastroEndereco(object):
    repositorio = BaseRepositorio

    def __init__(self, repositorio_factory):
        self.repositorio = repositorio_factory.repositorio_factory()

    def cadastrar(self, endereco):
        return self.repositorio.cadastrar(endereco)

    def buscar(self, cep, numero):
        return self.repositorio.buscar(cep, numero)

    def atualizar(self, cep, numero, **kwargs):
        return self.repositorio.atualizar(cep, numero, **kwargs)

    def remover(self, **kwargs):
        return self.repositorio.remover(**kwargs)

    def listar_todos(self):
        return self.repositorio.listar_todos()
