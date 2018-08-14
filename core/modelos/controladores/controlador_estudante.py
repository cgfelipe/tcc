from core.modelos import CadastroEstudante
from core.modelos import RepositorioFactory

class ControladorEstudante(object):
     cadastro_estudante = CadastroEstudante(RepositorioFactory())

    def cadastrar(self, estudante):
        return self.cadastro_estudante.cadastrar(estudante)

    def buscar(self, cpf):
        return self.cadastro_estudante.buscar(cpf)

    def listar_todos(self):
        return self.cadastro_estudante.listar_todos()

    def atualizar(self, cpf, **kwargs):
        return self.cadastro_estudante.atualizar(cpf, **kwargs)

    def remover(self, **kwargs):
        return self.cadastro_estudante.remover(**kwargs)

