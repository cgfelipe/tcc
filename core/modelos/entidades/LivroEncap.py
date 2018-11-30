class Livro:

    __titulo = ""
    __dataCriacao = ""
    __autores = ""
    __editora = ""
    __edicao = ""
    __ano = 0
    __valor = 0.0
    __disciplinas = ""
    __estudante = ""
    __emprestado = ""

    def __init__(self, titulo, dataCriacao, autores, editora, edicao, ano, valor, disciplinas, estudante, emprestado):
        self.__titulo = titulo
        self.__dataCriacao = dataCriacao
        self.__estudante = estudante
        self.__autores = autores
        self.__edicao = edicao
        self.__ano = ano
        self.__valor = valor
        self.__editora = editora
        self.__emprestado = emprestado
        self.__disciplinas = disciplinas

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def dataCriacao(self):
        return self.__dataCriacao

    @dataCriacao.setter
    def data(self, dataCriacao):
        self.__dataCriacao = dataCriacao

    @property
    def autores(self):
        return self.__autores

    @autores.setter
    def autores(self, autores):
        self.__autores = autores

    @property
    def editora(self):
        return self.__editora

    @editora.setter
    def editora(self, editora):
        self.__editora = editora

    @property
    def edicao(self):
        return self.__edicao

    @edicao.setter
    def edicao(self, edicao):
        self.__edicao = edicao

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def estudante(self):
        return self.__estudante

    @estudante.setter
    def estudante(self, estudante):
        self.__estudante = estudante

    @property
    def emprestado(self):
        return self.__emprestado

    @emprestado.setter
    def emprestado(self, emprestado):
        self.__emprestado = emprestado

    @property
    def disciplinas(self):
        return self.__disciplinas

    @disciplinas.setter
    def disciplinas(self, disciplinas):
        self.__disciplinas = disciplinas