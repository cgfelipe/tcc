from core.modelos.cadastros.cadastro_departamento import CadastroDepartamento
from core.modelos import RepositorioFactory


class ControladorDepartamento(object):
     cadastro_departamento = CadastroDepartamento(RepositorioFactory())

    def cadastrar(self, departamento):
        return self.cadastro_departamento.cadastrar(departamento)

    def buscar(self, nome):
        return self.cadastro_departamento.buscar(nome)

    def listar_todos(self):
        return self.cadastro_departamento.listar_todos()

    def atualizar(self, nome, **kwargs):
        return self.cadastro_departamento.atualizar(nome, **kwargs)

    def remover(self, **kwargs):
        return self.cadastro_departamento.remover(**kwargs)
