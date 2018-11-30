class Artigo:

    __titulo = ""
    __data = ""
    __estudante = None
    __professor = None
    __resumo = ""
    __paginas = 0
    __nota = 0.0
    __classificacao = ""
    __apresentacao = False
    __disciplina = ""

    def __init__(self, titulo, data, estudante, professor, resumo, paginas, nota, classificacao, apresentacao, disciplina):
        self.__titulo = titulo
        self.__data = data
        self.__estudante = estudante
        self.__professor = professor
        self.__resumo = resumo
        self.__paginas = paginas
        self.__nota = nota
        self.__classificacao = classificacao
        self.__apresentacao = apresentacao
        self.__disciplina = disciplina

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def estudante(self):
        return self.__estudante

    @estudante.setter
    def estudante(self, estudante):
        self.__estudante = estudante

    @property
    def professor(self):
        return self.__professor

    @professor.setter
    def professor(self, professor):
        self.__professor = professor

    @property
    def resumo(self):
        return self.__resumo

    @resumo.setter
    def resumo(self, resumo):
        self.__resumo = resumo

    @property
    def paginas(self):
        return self.__paginas

    @paginas.setter
    def paginas(self, paginas):
        self.__paginas = paginas

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, nota):
        self.__nota = nota

    @property
    def classificacao(self):
        return self.__classificacao

    @classificacao.setter
    def classificacao(self, classificacao):
        self.__classificacao = classificacao

    @property
    def apresentacao(self):
        return self.__apresentacao

    @apresentacao.setter
    def apresentacao(self, apresentacao):
        self.__apresentacao = apresentacao

    @property
    def disciplina(self):
        return self.__disciplina

    @disciplina.setter
    def disciplina(self, disciplina):
        self.__disciplina = disciplina