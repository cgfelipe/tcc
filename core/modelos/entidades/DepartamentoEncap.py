class DepartamentoEncap:

    __id = ""
    __nome = ""
    __dataFundacao = ""
    __diretor = None
    __quantidadeSalas = ""
    __rendaAnual = ""
    __cursos = None
    __quantidadeAlunos = 0
    __quantidadeProfessores = 0
    __descricao = ""
    __siglaDepartamento = ""

    def __init__(self, id, nome, dataFundacao, diretor, quantidadeSalas, rendaAnual, cursos, quantidadeAlunos, quantidadeProfessores, descricao, sigla):
        self.__id = id
        self.__nome = nome
        self.__dataFundacao = dataFundacao
        self.__diretor = diretor
        self.__quantidadeSalas = quantidadeSalas
        self.__rendaAnual = rendaAnual
        self.__cursos = cursos
        self.__descricao = descricao
        self.__quantidadeAlunos = quantidadeAlunos
        self.__quantidadeProfessores = quantidadeProfessores
        self.__siglaDepartamento = sigla

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def dataFundacao(self):
        return self.__dataFundacao

    @dataFundacao.setter
    def dataFundacao(self, dataFundacao):
        self.__dataFundacao = dataFundacao

    @property
    def diretor(self):
        return self.__diretor

    @diretor.setter
    def diretor(self, diretor):
        self.__diretor = diretor

    @property
    def quantidadeSalas(self):
        return self.__quantidadeSalas

    @quantidadeSalas.setter
    def quantidadeSalas(self, quantidadeSalas):
        self.__quantidadeSalas = quantidadeSalas

    @property
    def rendaAnual(self):
        return self.__rendaAnual

    @rendaAnual.setter
    def rendaAnual(self, rendaAnual):
        self.__rendaAnual = rendaAnual

    @property
    def cursos(self):
        return self.__cursos

    @cursos.setter
    def cursos(self, cursos):
        self.__cursos = cursos

    @property
    def quantidadeProfessores(self):
        return self.__quantidadeProfessores

    @quantidadeProfessores.setter
    def quantidadeProfessores(self, quantidadeProfessores):
        self.__quantidadeProfessores = quantidadeProfessores

    @property
    def quantidadeAlunos(self):
        return self.__quantidadeAlunos

    @quantidadeAlunos.setter
    def quantidadeAlunos(self, quantidadeAlunos):
        self.__quantidadeAlunos = quantidadeAlunos

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def siglaDepartamento(self):
        return self.__siglaDepartamento

    @siglaDepartamento.setter
    def siglaDepartamento(self, siglaDepartamento):
        self.__siglaDepartamento = siglaDepartamento
