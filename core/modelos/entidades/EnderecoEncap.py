class Endereco:

    __cep = ""
    __logradouro = ""
    __numero = ""
    __complemento = ""
    __referencia = ""
    __bairro = ""
    __cidade = ""
    __estado = ""
    __pais = ""

    def __init__(self, cep, logradouro, numero, complemento, referencia, bairro, cidade, estado, pais):
        self.__cep = cep
        self.__logradouro = logradouro
        self.__numero = numero
        self.__complemento = complemento
        self.__referencia = referencia
        self.__bairro = bairro
        self.__cidade = cidade
        self.__estado = estado
        self.__pais = pais

    @property
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self, cep):
        self.__cep = cep

    @property
    def logradouro(self):
        return self.__logradouro

    @logradouro.setter
    def logradouro(self, logradouro):
        self.__logradouro = logradouro

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def complemento(self):
        return self.__complemento

    @complemento.setter
    def complemento(self, complemento):
        self.__complemento = complemento

    @property
    def referencia(self):
        return self.__referencia

    @referencia.setter
    def referencia(self, referencia):
        self.__referencia = referencia

    @property
    def bairro(self):
        return self.__bairro

    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    @property
    def pais(self):
        return self.__pais

    @pais.setter
    def pais(self, pais):
        self.__pais = pais
