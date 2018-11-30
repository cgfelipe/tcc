class Pessoa:

    __nome = ""
    __email = ""
    __cpf = ""
    __usuario = ""
    __senha = ""
    __data_nascimento = ""

    def __init__(self, nome, email, cpf, usuario, senha, data_nascimento):
        self.__nome = nome
        self.__email = email
        self.__cpf = cpf
        self.__usuario = usuario
        self.__senha = senha
        self.__data_nascimento = data_nascimento

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento
