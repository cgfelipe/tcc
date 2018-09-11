from core.modelos.cadastros.cadastro_curriculo import CadastroCurriculo
from core.modelos import RepositorioFactory


class ControladorCurriculo(object):
     cadastro_curriculo = CadastroCurriculo(RepositorioFactory())

    def cadastrar(self, curriculo):
        return self.cadastro_curriculo.cadastrar(curriculo)

    def buscar(self, idLattes):
        return self.cadastro_curriculo.buscar(idLattes)

    def listar_todos(self):
        return self.cadastro_curriculo.listar_todos()

    def atualizar(self, idLattes, **kwargs):
        return self.cadastro_curriculo.atualizar(idLattes, **kwargs)

    def remover(self, **kwargs):
        return self.cadastro_curriculo.remover(**kwargs)
