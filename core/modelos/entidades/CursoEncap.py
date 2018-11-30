class Curso:

    __id = ""
    __nome_curso = ""

    def __init__(self, id, nome_curso):
        self.__id = id
        self.__nome_curso = nome_curso

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nome_curso(self):
        return self.__nome_curso

    @nome_curso.setter
    def nome_curso(self, nome_curso):
        self.__nome_curso = nome_curso
