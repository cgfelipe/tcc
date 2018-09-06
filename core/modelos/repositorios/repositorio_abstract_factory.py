from core.modelos.repositorios.repositorio_endereco import RepositorioEndereco
from core.modelos.repositorios.repositorio_estudante import RepositorioEstudante
from core.modelos.repositorios.repositorio_professor import RepositorioProfessor


class RepositorioFactory(object):
    @staticmethod
    def factory(_type):
        if 'endereco' in _type:
            return RepositorioEndereco()
        elif 'estudante' in _type:
            return RepositorioEstudante()
        elif professor'' in _type:
            return RepositorioProfessor()
        raise Exception('Invalid type ' + _type)
