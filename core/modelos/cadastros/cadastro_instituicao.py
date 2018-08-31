from core.modelos.repositorios.base_repositorio import BaseRepositorio


class CadastroInstituicao(object):
    repositorio = BaseRepositorio

    def __init__(self, repositorio_factory):
        self.repositorio = repositorio_factory.repositorio_factory()

    def cadastrar(self, instituicao):
        return self.repositorio.cadastrar(instituicao)

    def buscar(self, cnpj):
        return self.repositorio.buscar(cnpj)

    def atualizar(self, cnpj, **kwargs):
        return self.repositorio.atualizar(cnpj, **kwargs)

    def remover(self, **kwargs):
        return self.repositorio.remover(**kwargs)

    def listar_todos(self):
        return self.repositorio.listar_todos()
