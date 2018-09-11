from core.modelos.repositorios.base_repositorio import BaseRepositorio


class CadastroProjetoPesquisa(object):
    repositorio = BaseRepositorio

    def __init__(self, repositorio_factory):
        self.repositorio = repositorio_factory.repositorio_factory()

    def cadastrar(self, projeto_pesquisa):
        return self.repositorio.cadastrar(projeto_pesquisa)

    def buscar(self, idLattes):
        return self.repositorio.buscar(idLattes)

    def atualizar(self, idLattes, **kwargs):
        return self.repositorio.atualizar(idLattes, **kwargs)

    def remover(self, **kwargs):
        return self.repositorio.remover(**kwargs)

    def listar_todos(self):
        return self.repositorio.listar_todos()
