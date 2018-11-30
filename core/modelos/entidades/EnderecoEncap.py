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
