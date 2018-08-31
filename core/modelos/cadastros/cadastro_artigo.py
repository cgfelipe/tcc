from core.modelos.repositorios.base_repositorio import BaseRepositorio


class CadastroArtigo(object):
    repositorio = BaseRepositorio

    def __init__(self, repositorio_factory):
        self.repositorio = repositorio_factory.repositorio_factory()

    def cadastrar(self, artigo):
        return self.repositorio.cadastrar(artigo)

    def buscar(self, titulo):
        return self.repositorio.buscar(titulo)

    def atualizar(self, titulo, **kwargs):
        return self.repositorio.atualizar(titulo, **kwargs)

    def remover(self, **kwargs):
        return self.repositorio.remover(**kwargs)

    def listar_todos(self):
        return self.repositorio.listar_todos()
