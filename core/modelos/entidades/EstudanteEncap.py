class Estudante:

    __matricula = ""
    __escolaridade = ""
    __dataMatricula = ""
    __dataColacao = ""
    __usosRestauranteUniversitario = ""
    __coeficienteRendimento = 0.0
    __bolsista = False
    __bolsa = 0.0
    __agenciaBancaria = ""
    __contaBancaria = ""
    __pessoa = None

    def __init__(self, matricula, escolaridade, dataMatricula, dataColacao, usosRestauranteUniversitario, coeficienteRendimento, bolsista, bolsa, agenciaBancaria, contaBancaria):
        self.__matricula = matricula
        self.__escolaridade = escolaridade
        self.__agenciaBancaria = agenciaBancaria
        self.__dataMatricula = dataMatricula
        self.__usosRestauranteUniversitario = usosRestauranteUniversitario
        self.__coeficienteRendimento = coeficienteRendimento
        self.__bolsista = bolsista
        self.__dataColacao = dataColacao
        self.__contaBancaria = contaBancaria
        self.__bolsa = bolsa

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def escolaridade(self):
        return self.__escolaridade

    @escolaridade.setter
    def data(self, escolaridade):
        self.__escolaridade = escolaridade

    @property
    def dataMatricula(self):
        return self.__dataMatricula

    @dataMatricula.setter
    def dataMatricula(self, dataMatricula):
        self.__dataMatricula = dataMatricula

    @property
    def dataColacao(self):
        return self.__dataColacao

    @dataColacao.setter
    def dataColacao(self, dataColacao):
        self.__dataColacao = dataColacao

    @property
    def usosRestauranteUniversitario(self):
        return self.__usosRestauranteUniversitario

    @usosRestauranteUniversitario.setter
    def usosRestauranteUniversitario(self, usosRestauranteUniversitario):
        self.__usosRestauranteUniversitario = usosRestauranteUniversitario

    @property
    def coeficienteRendimento(self):
        return self.__coeficienteRendimento

    @coeficienteRendimento.setter
    def coeficienteRendimento(self, coeficienteRendimento):
        self.__coeficienteRendimento = coeficienteRendimento

    @property
    def bolsista(self):
        return self.__bolsista

    @bolsista.setter
    def bolsista(self, bolsista):
        self.__bolsista = bolsista

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
    def bolsa(self):
        return self.__bolsa

    @bolsa.setter
    def bolsa(self, bolsa):
        self.__bolsa = bolsa