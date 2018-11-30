class Instituicao:

    __nome = ""
    __cnpj = ""
    __fundador = None
    __endereco = None
    __dataFundacao = ""
    __site = ""
    __telefone = ""
    __numeroFuncionarios = 0
    __listaDepartamentos = ""
    __renda = 0.0

    def __init__(self, nome, cnpj, fundador, endereco, dataFundacao, site, telefone, numeroFuncionarios, listaDepartamentos, renda):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__fundador = fundador
        self.__dataFundacao = dataFundacao
        self.__site = site
        self.__telefone = telefone
        self.__endereco = endereco
        self.__numeroFuncionarios = numeroFuncionarios
        self.__listaDepartamentos = listaDepartamentos
        self.__renda = renda

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

    @property
    def fundador(self):
        return self.__fundador

    @fundador.setter
    def fundador(self, fundador):
        self.__fundador = fundador

    @property
    def dataFundacao(self):
        return self.__dataFundacao

    @dataFundacao.setter
    def dataFundacao(self, dataFundacao):
        self.__dataFundacao = dataFundacao

    @property
    def site(self):
        return self.__site

    @site.setter
    def site(self, site):
        self.__site = site

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def numeroFuncionarios(self):
        return self.__numeroFuncionarios

    @numeroFuncionarios.setter
    def numeroFuncionarios(self, numeroFuncionarios):
        self.__numeroFuncionarios = numeroFuncionarios

    @property
    def listaDepartamentos(self):
        return self.__listaDepartamentos

    @listaDepartamentos.setter
    def listaDepartamentos(self, listaDepartamentos):
        self.__listaDepartamentos = listaDepartamentos

    @property
    def renda(self):
        return self.__renda

    @renda.setter
    def renda(self, renda):
        self.__renda = renda