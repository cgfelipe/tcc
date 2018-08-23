from core.modelos.repositorios.base_repositorio import BaseRepositorio
from core.modelos.cadastros.cadastro_pessoa import CadastroPessoa


class CadastroProfessor(CadastroPessoa):
    repositorio = BaseRepositorio

    def __init__(self, repositorio_factory):
        super(CadastroProfessor, self).__init__(
            repositorio_factory, 'professor')
