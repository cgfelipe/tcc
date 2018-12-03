from django.db import models


class Base(object):
    def serialize(self):
        return vars(self)

# Create your models here.


class Endereco(Base, models.Model):
    id = models.AutoField(primary_key=True)
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=20)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=5)
    referencia = models.CharField(max_length=10)
    bairro = models.CharField(max_length=10)
    cidade = models.CharField(max_length=10)
    estado = models.CharField(max_length=2)
    pais = models.CharField(max_length=10)

    def __str__(self):
        return self.logradouro

    @staticmethod
    def buscar(_cep, _numero):
        return Endereco.objects.get(cep=_cep, numero=_numero)

    @staticmethod
    def listar_todos(self):
        return Endereco.objects.all()

    def atualizar(self, **kwargs):
        return self.update(**kwargs)

    def remover(self, **kwargs):
        return self.cadastro_endereco.remover(**kwargs)


class Especialidade(models.Model):
    titulo = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo

    @staticmethod
    def buscar(_id):
        return Especialidade.objects.get(id=_id)

    @staticmethod
    def listar_todos():
        return Especialidade.objects.all()

    def atualizar(self, **kwargs):
        return self.update(**kwargs)

    def remover(self, **kwargs):
        return self.delete()


class Escolaridade(models.Model):
    titulo = models.CharField(max_length=30)

    def __str__(self):
        return self.titulo

    @staticmethod
    def buscar(_titulo):
        return Escolaridade.objects.get(titulo=_titulo)

    @staticmethod
    def listar_todos():
        return Escolaridade.objects.all()

    def atualizar(self, **kwargs):
        return self.update(**kwargs)

    def remover(self, **kwargs):
        return self.delete()


class Pessoa(Base, models.Model):
    nome = models.CharField(max_length=200)
    nomeMae = models.CharField(max_length=200)
    dataNascimento = models.DateField(null=True)
    email = models.CharField(max_length=50)
    telefone = models.CharField(max_length=30)
    endereco = models.ForeignKey(to=Endereco, on_delete=models.CASCADE, verbose_name="Endereço", null=True)
    usuario = models.CharField(max_length=20)
    senha = models.CharField(max_length=50)
    cpf = models.CharField(unique=True, max_length=11)
    rg = models.CharField(max_length=8)

    def __str__(self):
        return self.nome

    @classmethod
    def buscar(cls, cpf):
        return cls.objects.get(cpf=cpf)

    def atualizar(self, **kwargs):
        return self.update(**kwargs)

    def remover(self, **kwargs):
        return self.delete

    @classmethod
    def listar_todos(cls):
        return [o.serialize() for o in cls.objects.all()]


class Professor(Pessoa):
    escolaridade = models.ForeignKey(
        to=Escolaridade, on_delete=models.CASCADE, null=False, verbose_name='escolaridade do professor')
    inscricao = models.CharField(max_length=10, null=False)
    dataAdmissao = models.DateField(null=False)
    interino = models.BooleanField(null=False)
    concursado = models.BooleanField(null=False)
    especialidade = models.ForeignKey(
        Especialidade, on_delete=models.CASCADE, null=False, verbose_name='especialidades do professor'
    )
    salario = models.FloatField(null=False)
    agenciaBancaria = models.CharField(max_length=10)
    contaBancaria = models.CharField(max_length=10)
    projetos = models.CharField(max_length=500)

    def __str__(self):
        return self.nome

    @staticmethod
    def buscar(_id):
        return Professor.objects.get(id=_id)

    @staticmethod
    def listar_todos():
        return Professor.objects.all()

    def atualizar(self, **kwargs):
        return self.update(**kwargs)

    def remover(self, **kwargs):
        return self.delete()


class Estudante(Pessoa):
    matricula = models.CharField(unique=True, max_length=11)
    escolaridade = models.ForeignKey(
        to=Escolaridade, on_delete=models.CASCADE, null=False, verbose_name='escolaridade do aluno')
    dataMatricula = models.DateField()
    dataColacao = models.DateField()
    usosRestauranteUniversitario = models.IntegerField()
    coeficienteRendimento = models.FloatField()
    bolsista = models.BooleanField()
    bolsa = models.FloatField()
    agenciaBancaria = models.CharField(max_length=200)
    contaBancaria = models.CharField(max_length=200)

    def __str__(self):
        return self.matricula

    @staticmethod
    def buscar(_id):
        return Estudante.objects.get(id=_id)

    @staticmethod
    def listar_todos():
        return Estudante.objects.all()

    def atualizar(self, **kwargs):
        return self.update(**kwargs)

    def remover(self, **kwargs):
        return self.delete()


class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    nome_curso = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_curso

    @staticmethod
    def buscar(_id):
        return Curso.objects.get(id=id)

    @staticmethod
    def listar_todos():
        return Curso.objects.all()

    def atualizar(self, **kwargs):
        return self.update(**kwargs)

    def remover(self, **kwargs):
        return self.delete()


class Departamento(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)
    dataFundacao = models.DateField()
    diretor = models.OneToOneField(
        Professor, on_delete=models.CASCADE, null=False, verbose_name='diretor do departamento'
    )
    quantidadeSalas = models.IntegerField()
    quantidadeAlunos = models.IntegerField(null=True)
    quantidadeProfessores = models.IntegerField(null=True)
    descricao = models.CharField(max_length=500, null=True)
    siglaDepartamento = models.CharField(max_length=3, null=True, verbose_name='sigla do departamento')
    rendaAnual = models.FloatField()
    cursos = models.ManyToManyField(to=Curso, null=False)

    def __str__(self):
        return self.nome

    @staticmethod
    def buscar(_nome):
        return Departamento.objects.get(nome=_nome)

    @staticmethod
    def listar_todos():
        return Departamento.objects.all()

    def atualizar(self, **kwargs):
        return self.update(**kwargs)

    def remover(self, **kwargs):
        return self.delete()


class Curriculo(Base, models.Model):
    id = models.AutoField(primary_key=True)
    objetivo = models.CharField(max_length=500)
    pessoa = models.OneToOneField(
        Pessoa, on_delete=models.CASCADE, null=False, verbose_name='responsavel do curriculo')
    idLattes = models.CharField(max_length=10)
    pretensaoSalarial = models.FloatField()
    ultimaAtualizacao = models.DateField()
    titulo = models.CharField(max_length=30)
    endereco = models.ForeignKey(
        to=Endereco, on_delete=models.CASCADE, null=False, verbose_name='endereco do curriculo')
    experiencia = models.CharField(max_length=500)
    competencias = models.CharField(max_length=500)
    formacoes = models.CharField(max_length=500)

    @staticmethod
    def buscar(_idLattes):
        return Curriculo.objects.get(idLattes=_idLattes)

    @staticmethod
    def listar_todos():
        return Curriculo.objects.all()

    def atualizar(self, **kwargs):
        return self.update(**kwargs)

    def remover(self, **kwargs):
        return self.delete()


class Artigo(Base, models.Model):
    titulo = models.CharField(max_length=20)
    data = models.DateField()
    estudante = models.ForeignKey(
        to=Estudante, on_delete=models.CASCADE, null=False, verbose_name='estudante responsavel')
    professor = models.ForeignKey(
        to=Professor, on_delete=models.CASCADE, null=False, verbose_name='professor orientador')
    resumo = models.CharField(max_length=500)
    paginas = models.IntegerField()
    nota = models.FloatField()
    classificacao = models.CharField(max_length=10)
    apresentacao = models.BooleanField()
    disciplina = models.CharField(max_length=20)

    @staticmethod
    def buscar(_titulo):
        return Artigo.objects.get(titulo=_titulo)

    @staticmethod
    def listar_todos():
        return Artigo.objects.all()

    def atualizar(self, **kwargs):
        return self.update(**kwargs)

    def remover(self, **kwargs):
        return self.delete()


class Instituicao(models.Model):
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(primary_key=True, max_length=15)
    endereco = models.OneToOneField(
        Endereco, on_delete=models.CASCADE, null=False, verbose_name='endereço da instituição')
    fundador = models.OneToOneField(
        Pessoa, on_delete=models.CASCADE, null=False, verbose_name='fundador da instituição')
    dataFundacao = models.DateField()
    site = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11)
    numeroFuncionarios = models.IntegerField()
    departamentos = models.ForeignKey(
        Departamento, on_delete=models.CASCADE, verbose_name='lista de departamentos')
    rendaAnual = models.FloatField()

    @staticmethod
    def buscar(_cnpj):
        return Instituicao.objects.get(cnpj=_cnpj)

    @staticmethod
    def listar_todos():
        return Instituicao.objects.all()

    def atualizar(self, **kwargs):
        return self.update(**kwargs)

    def remover(self, **kwargs):
        return self.delete()


class Livro(models.Model):
    titulo = models.CharField(max_length=50)
    autores = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    edicao = models.IntegerField()
    valor = models.FloatField()
    dataCriacao = models.DateField()
    ano = models.IntegerField()
    disciplinas = models.CharField(max_length=50)
    estudante = models.ForeignKey(
        to=Estudante, on_delete=models.CASCADE, null=False, verbose_name='estudante que usa o livro')
    emprestado = models.BooleanField()


    @staticmethod
    def buscar(_titulo):
        return Livro.objects.get(titulo=_titulo)

    @staticmethod
    def listar_todos():
        return Livro.objects.all()

    def atualizar(self, **kwargs):
        return self.update(**kwargs)

    def remover(self, **kwargs):
        return self.delete()


class ProjetoDePesquisa(models.Model):
    id = models.AutoField(primary_key=True)
    idLattes = models.CharField(max_length=7)
    titulo = models.CharField(max_length=50)
    inicio = models.DateField()
    fim = models.DateField()
    keywords = models.CharField(max_length=50)
    valorProjeto = models.FloatField()
    situacao = models.CharField(max_length=100)
    alunos = models.CharField(max_length=50)
    professor = models.ForeignKey(
        to=Professor, on_delete=models.CASCADE, null=False, verbose_name='professor orientador')
    departamentoResponsavel = models.ForeignKey(
        to=Departamento, on_delete=models.CASCADE, null=False, verbose_name='departamento responsavel')

    @staticmethod
    def buscar(_idLattes):
        return ProjetoDePesquisa.objects.get(idLattes=_idLattes)

    @staticmethod
    def listar_todos():
        return ProjetoDePesquisa.objects.all()

    def atualizar(self, **kwargs):
        return self.update(**kwargs)

    def remover(self, **kwargs):
        return self.delete()
