from core.modelos.cadastros.cadastro_artigo import CadastroArtigo
from core.modelos import RepositorioFactory


class ControladorArtigo(object):
     cadastro_artigo = CadastroArtigo(RepositorioFactory())

    def cadastrar(self, artigo):
        return self.cadastro_artigo.cadastrar(artigo)

    def buscar(self, titulo):
        return self.cadastro_artigo.buscar(titulo)

    def listar_todos(self):
        return self.cadastro_artigo.listar_todos()

    def atualizar(self, titulo, **kwargs):
        return self.cadastro_artigo.atualizar(titulo, **kwargs)

    def remover(self, **kwargs):
        return self.cadastro_artigo.remover(**kwargs)
