from core.modelos.cadastros.cadastro_instituicao import CadastroInstituicao
from core.modelos import RepositorioFactory


class ControladorInstituicao(object):
     cadastro_instituicao = CadastroInstituicao(RepositorioFactory())

    def cadastrar(self, instituicao):
        return self.cadastro_instituicao.cadastrar(instituicao)

    def buscar(self, cnpj):
        return self.cadastro_instituicao.buscar(cnpj)

    def listar_todos(self):
        return self.cadastro_instituicao.listar_todos()

    def atualizar(self, cnpj, **kwargs):
        return self.cadastro_instituicao.atualizar(cnpj, **kwargs)

    def remover(self, **kwargs):
        return self.cadastro_instituicao.remover(**kwargs)
