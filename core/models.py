from django.db import models

class Base(object):
    def serialize(self):
        return vars(self)

# Create your models here.
class Artigo(Base, models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateField()
    estudante = models.OneToOneField(
        Estudante, on_delete=models.CASCADE, null=False, verbose_name='estudante responsavel')
    professor = models.OneToOneField(
        Professor, on_delete=models.CASCADE, null=False, verbose_name='professor orientador')
    resumo = models.CharField(max_length=500)
    paginas = models.IntegerField()
    nota = models.FloatField()
    classificacao = models.CharField(max_length=10)
    apresentacao = models.BooleanField()
    disciplina = models.CharField(max_length=30)

    @staticmethod
    def buscar(_id):
        return Artigo.objects.get(id = _id)

    @staticmethod
    def listar_todos():
        return Artigo.objects.all()

    def atualizar(self, **kwargs):
        return self.update(**kwargs)

    def remover(self, **kwargs):
        return self.delete()

class Curriculo(Base, models.Model):
    objetivo = models.CharField(max_lenght=500)
    pessoa = models.OneToOneField(
        Pessoa, on_delete=models.CASCADE, null=False, verbose_name='responsavel do curriculo')
    idLattes = models.CharField(max_lenght=10)
    pretensaoSalarial = models.FloatField()
    ultimaAtualizacao = models.DateField()
    titulo = models.CharField(max_lenght=30)
    endereco = models.OneToOneField(
        Endereco, on_delete=models.CASCADE, null=False, verbose_name='endereco do curriculo')
    experiencia = models.CharField(max_lenght=500)
    competencias = models.CharField(max_lenght=500)
    formacoes = models.CharField(max_lenght=500)


class Pessoa(Base, models.Model):
    nome = models.CharField(max_length=200)
    nomeMae = models.CharField(max_length=200)
    dataNascimento = models.DateField()
    email = models.CharField(max_length=50)
    telefone = models.CharField(max_length=30)
    endereco = models.OneToOneField(
        Endereco, on_delete=models.CASCADE, null=False, verbose_name='endereço da pessoa')
    usuario = models.CharField(max_length=20)
    senha = models.CharField(max_length=50)
    cpf = models.CharField(primary_key=True, max_lenght=11)
    rg = models.CharField(max_length=8)

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
    escolaridade = models.OneToOneField(
        Escolaridade, on_delete=models.CASCADE, null=False, verbose_name='escolaridade do professor')
    inscricao = models.CharField(max_length=10, null=False)
    dataAdmissao = models.DateField(null=False)
    interino = models.BooleanField(null=False)
    concursado = models.BooleanField(null=False)
    especialidade = models.ForeignKey(
        Especialidade, on_delete=models.CASCADE, null=False, verbose_name='especialidades do professor'
    )
    salario = models.FloatField(null=False)
    agenciaBancaria = models.CharField()
    contaBancaria = models.CharField()
    projetos = models.CharField(max_length=500)


class Estudante(Pessoa):
    matricula = models.CharField(primary_key=True, max_lenght=11)
    escolaridade = models.OneToOneField(
        Escolaridade, on_delete=models.CASCADE, null=False, verbose_name='escolaridade do aluno')
    dataMatricula = models.DateField()
    dataColacao = models.DateField()
    usosRestauranteUniversitario = models.IntegerField()
    coeficienteRendimento = models.FloatField()
    bolsista = models.BooleanField()
    bolsa = models.FloatField()
    agenciaBancaria = models.CharField()
    contaBancaria = models.CharField()
