class ProfessorEncap:

    __escolaridade = None
    __inscricao = ""
    __dataAdmissao = ""
    __interino = None
    __concursado = None
    __especialidade = None
    __salario = ""
    __agenciaBancaria = ""
    __contaBancaria = ""
    __projetos = ""

    def __init__(self, escolaridade, inscricao, dataAdmissao, interino, concursado, especialidade, salario, agenciaBancaria, contaBancaria, projetos):
        self.__escolaridade = escolaridade
        self.__inscricao = inscricao
        self.__dataAdmissao = dataAdmissao
        self.__interino = interino
        self.__concursado = concursado
        self.__especialidade = especialidade
        self.__salario = salario
        self.__agenciaBancaria = agenciaBancaria
        self.__contaBancaria = contaBancaria
        self.__projetos = projetos

    @property
    def escolaridade(self):
        return self.__escolaridade

    @escolaridade.setter
    def escolaridade(self, escolaridade):
        self.__escolaridade = escolaridade

    @property
    def inscricao(self):
        return self.__inscricao

    @inscricao.setter
    def inscricao(self, inscricao):
        self.__inscricao = inscricao

    @property
    def dataAdmissao(self):
        return self.__dataAdmissao

    @dataAdmissao.setter
    def dataAdmissao(self, dataAdmissao):
        self.__dataAdmissao = dataAdmissao

    @property
    def interino(self):
        return self.__interino

    @interino.setter
    def interino(self, interino):
        self.__interino = interino

    @property
    def concursado(self):
        return self.__concursado

    @concursado.setter
    def concursado(self, concursado):
        self.__concursado = concursado

    @property
    def especialidade(self):
        return self.__especialidade

    @especialidade.setter
    def especialidade(self, especialidade):
        self.__especialidade = especialidade

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    @property
    def agenciaBancaria(self):
        return self.__agenciaBancaria

    @agenciaBancaria.setter
    def agenciaBancaria(self, agenciaBancaria):
        self.__agenciaBancaria = agenciaBancaria

    @property
    def contaBancaria(self):
        return self.__contaBancaria

    @contaBancaria.setter
    def contaBancaria(self, contaBancaria):
        self.__contaBancaria = contaBancaria

    @property
    def projetos(self):
        return self.__projetos

    @projetos.setter
    def projetos(self, projetos):
        self.__projetos = projetos
