from core.modelos.cadastros.cadastro_escolaridade import CadastroEscolaridade
from core.modelos import RepositorioFactory


class ControladorEscolaridade(object):
     cadastro_escolaridade = CadastroEscolaridade(RepositorioFactory())

    def cadastrar(self, escolaridade):
        return self.cadastro_escolaridade.cadastrar(escolaridade)

    def buscar(self, titulo):
        return self.cadastro_escolaridade.buscar(titulo)

    def listar_todos(self):
        return self.cadastro_escolaridade.listar_todos()

    def atualizar(self, titulo, **kwargs):
        return self.cadastro_escolaridade.atualizar(titulo, **kwargs)

    def remover(self, **kwargs):
        return self.cadastro_escolaridade.remover(**kwargs)
