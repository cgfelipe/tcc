from core.models import CadastroProfessor
from core.models import RepositoryFactory

class ControladorProfessor(object):
    cadastro_professor = CadastroProfessor(RepositorioFactory())

     def cadastrar(self, professor):
         return self.cadastro_professor.cadastrar(professor)

    def buscar(self, cpf):
        return self.cadastro_professor.buscar(cpf)

    def listar_todos(self):
        return self.cadastro_professor.listar_todos()

    def atualizar(self, cpf, **kwargs):
        return self.cadastro_professor.atualizar(cpf, **kwargs)

    def remover(self, **kwargs):
        return self.cadastro_professor.remover(**kwargs)
