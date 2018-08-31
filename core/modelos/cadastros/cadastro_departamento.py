from core.modelos.repositorios.base_repositorio import BaseRepositorio


class CadastroDepartamento(object):
    repositorio = BaseRepositorio

    def __init__(self, repositorio_factory):
        self.repositorio = repositorio_factory.repositorio_factory()

    def cadastrar(self, departamento):
        return self.repositorio.cadastrar(departamento)

    def buscar(self, nome):
        return self.repositorio.buscar(nome)

    def atualizar(self, nome, **kwargs):
        return self.repositorio.atualizar(nome, **kwargs)

    def remover(self, **kwargs):
        return self.repositorio.remover(**kwargs)

    def listar_todos(self):
        return self.repositorio.listar_todos()
