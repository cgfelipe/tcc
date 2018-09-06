from core.modelos.controladores.controlador_artigo import ControladorArtigo
from core.modelos.controladores.controlador_departamento import ControladorDepartamento
from core.modelos.controladores.controlador_endereco import ControladorEndereco
from core.modelos.controladores.controlador_estudante import ControladorEstudante
from core.modelos.controladores.controlador_instituicao import ControladorInstituicao
from core.modelos.controladores.controlador_professor import ControladorProfessor


class Fachada(object):

    @staticmethod
    def get_instance():
        return Fachada()
