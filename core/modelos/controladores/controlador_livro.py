from core.modelos.cadastros.cadastro_livro import CadastroLivro
from core.modelos import RepositorioFactory


class ControladorLivro(object):
     cadastro_livro = CadastroLivro(RepositorioFactory())

    def cadastrar(self, artigo):
        return self.cadastro_livro.cadastrar(artigo)

    def buscar(self, titulo):
        return self.cadastro_livro.buscar(titulo)

    def listar_todos(self):
        return self.cadastro_livro.listar_todos()

    def atualizar(self, titulo, **kwargs):
        return self.cadastro_livro.atualizar(titulo, **kwargs)

    def remover(self, **kwargs):
        return self.cadastro_livro.remover(**kwargs)
