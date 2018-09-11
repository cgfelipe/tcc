from core.modelos.cadastros.cadastro_especialidade import CadastroEspecialidade
from core.modelos import RepositorioFactory


class ControladorEspecialidade(object):
     cadastro_especialidade = CadastroEspecialidade(RepositorioFactory())

    def cadastrar(self, especialidade):
        return self.cadastro_especialidade.cadastrar(especialidade)

    def buscar(self, titulo):
        return self.cadastro_especialidade.buscar(titulo)

    def listar_todos(self):
        return self.cadastro_especialidade.listar_todos()

    def atualizar(self, titulo, **kwargs):
        return self.cadastro_especialidade.atualizar(titulo, **kwargs)

    def remover(self, **kwargs):
        return self.cadastro_especialidade.remover(**kwargs)
