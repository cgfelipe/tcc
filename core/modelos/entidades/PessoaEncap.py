class Pessoa:

    __nome = ""
    __nomeMae = ""
    __dataNascimento = ""
    __email = ""
    __telefone = ""
    __endereco = None
    __usuario = ""
    __senha = ""
    __cpf = ""
    __rg = ""

    def __init__(self, nome, nomeMae, dataNascimento, email, telefone, endereco, usuario, senha, cpf, rg):
        self.__nome = nome
        self.__nomeMae = nomeMae
        self.__dataNascimento = dataNascimento
        self.__email = email
        self.__telefone = telefone
        self.__endereco = endereco
        self.__usuario = usuario
        self.__senha = senha
        self.__cpf = cpf
        self.__rg = rg

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def nomeMae(self):
        return self.__nomeMae

    @nomeMae.setter
    def nomeMae(self, nomeMae):
        self.__nomeMae = nomeMae

    @property
    def dataNascimento(self):
        return self.__dataNascimento

    @dataNascimento.setter
    def dataNascimento(self, dataNascimento):
        self.__dataNascimento = dataNascimento

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

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
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def rg(self):
        return self.__rg

    @rg.setter
    def rg(self, rg):
        self.__rg = rg
