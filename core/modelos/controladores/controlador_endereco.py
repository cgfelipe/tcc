from core.modelos.cadastros.cadastro_endereco import CadastroEndereco
from core.modelos import RepositorioFactory


class ControladorEndereco(object):
     cadastro_endereco = CadastroEndereco(RepositorioFactory())

    def cadastrar(self, estudante):
        return self.cadastro_endereco.cadastrar(estudante)

    def buscar(self, cep, numero):
        return self.cadastro_endereco.buscar(cep, numero)

    def listar_todos(self):
        return self.cadastro_endereco.listar_todos()

    def atualizar(self, cep, numero, **kwargs):
        return self.cadastro_endereco.atualizar(cep, numero, **kwargs)

    def remover(self, **kwargs):
        return self.cadastro_endereco.remover(**kwargs)

