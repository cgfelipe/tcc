from core.modelos import BaseRepositorio
from core.modelos.cadastros.cadastro_pessoa import cadastro_pessoa

class CadastroEstudante(CadastroPessoa):
    repositorio = BaseRepositorio

     def __init__(self, repositorio_factory):
        super(CadastroEstudante, self).__init__(repositorio_factory, 'estudante')
    
