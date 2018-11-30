class ProjetoPesquisa:

    __inicio = ""
    __fim = ""
    __idLattes = 0
    __keywords = ""
    __valorProjeto = ""
    __titulo = ""
    __situacao = ""
    __alunos = ""
    __professorOrientador = None
    __departamentoResponsavel = None

    def __init__(self, titulo, inicio, responsaveCurriculo, idLattes, keywords, valorProjeto, situacao, alunos, professorOrientador, departamentoResponsavel):
        self.__titulo = titulo
        self.__inicio = inicio
        self.__fim = responsaveCurriculo
        self.__idLattes = idLattes
        self.__keywords = keywords
        self.__valorProjeto = valorProjeto
        self.__situacao = situacao
        self.__alunos = alunos
        self.__professorOrientador = professorOrientador
        self.__departamentoResponsavel = departamentoResponsavel

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def inicio(self):
        return self.__inicio

    @inicio.setter
    def inicio(self, inicio):
        self.__inicio = inicio

    @property
    def fim(self):
        return self.__fim

    @fim.setter
    def fim(self, fim):
        self.__fim = fim

    @property
    def idLattes(self):
        return self.__idLattes

    @idLattes.setter
    def idLattes(self, idLattes):
        self.__idLattes = idLattes

    @property
    def keywords(self):
        return self.__keywords

    @keywords.setter
    def keywords(self, keywords):
        self.__keywords = keywords

    @property
    def valorProjeto(self):
        return self.__valorProjeto

    @valorProjeto.setter
    def valorProjeto(self, valorProjeto):
        self.__valorProjeto = valorProjeto

    @property
    def situacao(self):
        return self.__situacao

    @situacao.setter
    def situacao(self, situacao):
        self.__situacao = situacao

    @property
    def alunos(self):
        return self.__alunos

    @alunos.setter
    def alunos(self, alunos):
        self.__alunos = alunos

    @property
    def professorOrientador(self):
        return self.__professorOrientador

    @professorOrientador.setter
    def professorOrientador(self, professorOrientador):
        self.__professorOrientador = professorOrientador

    @property
    def departamentoResponsavel(self):
        return self.__departamentoResponsavel

    @departamentoResponsavel.setter
    def departamentoResponsavel(self, departamentoResponsavel):
        self.__departamentoResponsavel = departamentoResponsavel