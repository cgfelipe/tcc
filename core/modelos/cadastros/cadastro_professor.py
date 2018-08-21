from core.modelos import BaseRepositorio
from core.modelos import CadastroPessoa

class CadastroProfessor(CadastroPessoa):
    repositorio = BaseRepositorio

    def __init__(self, repositorio_factory):
        super(CadastroProfessor, self).__init__(repositorio_factory, 'professor')