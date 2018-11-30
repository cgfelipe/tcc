class Curriculo:

    __objetivo = ""
    __responsavelCurriculo = ""
    __idLattes = 0
    __pretensaoSalarial = 0.0
    __ultimaAtualizacao = ""
    __titulo = ""
    __endereco = ""
    __experiencia = ""
    __competencias = ""
    __formacoes = ""

    def __init__(self, titulo, objetivo, responsaveCurriculo, idLattes, pretensaoSalarial, ultimaAtualizacao, endereco, experiencia, competencias, formacoes):
        self.__titulo = titulo
        self.__objetivo = objetivo
        self.__responsavelCurriculo = responsaveCurriculo
        self.__idLattes = idLattes
        self.__pretensaoSalarial = pretensaoSalarial
        self.__ultimaAtualizacao = ultimaAtualizacao
        self.__endereco = endereco
        self.__experiencia = experiencia
        self.__competencias = competencias
        self.__formacoes = formacoes

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def objetivo(self):
        return self.__objetivo

    @objetivo.setter
    def objetivo(self, objetivo):
        self.__objetivo = objetivo

    @property
    def responsavelCurriculo(self):
        return self.__responsavelCurriculo

    @responsavelCurriculo.setter
    def responsavelCurriculo(self, responsavelCurriculo):
        self.__responsavelCurriculo = responsavelCurriculo

    @property
    def idLattes(self):
        return self.__idLattes

    @idLattes.setter
    def idLattes(self, idLattes):
        self.__idLattes = idLattes

    @property
    def pretensaoSalarial(self):
        return self.__pretensaoSalarial

    @pretensaoSalarial.setter
    def pretensaoSalarial(self, pretensaoSalarial):
        self.__pretensaoSalarial = pretensaoSalarial

    @property
    def ultimaAtualizacao(self):
        return self.__ultimaAtualizacao

    @ultimaAtualizacao.setter
    def ultimaAtualizacao(self, ultimaAtualizacao):
        self.__ultimaAtualizacao = ultimaAtualizacao

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def experiencia(self):
        return self.__experiencia

    @experiencia.setter
    def experiencia(self, experiencia):
        self.__experiencia = experiencia

    @property
    def competencias(self):
        return self.__competencias

    @competencias.setter
    def competencias(self, competencias):
        self.__competencias = competencias

    @property
    def formacoes(self):
        return self.__formacoes

    @formacoes.setter
    def formacoes(self, formacoes):
        self.__formacoes = formacoes