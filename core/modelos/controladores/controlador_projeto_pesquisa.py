from core.modelos.cadastros.cadastro_projeto_pesquisa import CadastroProjetoPesquisa
from core.modelos import RepositorioFactory


class ControladorProjetoPesquisa(object):
     cadastro_projeto_pesquisa = CadastroProjetoPesquisa(RepositorioFactory())

    def cadastrar(self, curriculo):
        return self.cadastro_projeto_pesquisa.cadastrar(curriculo)

    def buscar(self, idLattes):
        return self.cadastro_projeto_pesquisa.buscar(idLattes)

    def listar_todos(self):
        return self.cadastro_projeto_pesquisa.listar_todos()

    def atualizar(self, idLattes, **kwargs):
        return self.cadastro_projeto_pesquisa.atualizar(idLattes, **kwargs)

    def remover(self, **kwargs):
        return self.cadastro_projeto_pesquisa.remover(**kwargs)
