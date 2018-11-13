from django import forms
from django.forms import ModelForm
from core import models


class EspecialidadeForm(ModelForm):
    class Meta:
        model = models.Especialidade
        fields = ['titulo']

class CursoForm(ModelForm):
    class Meta:
        model = models.Curso
        fields = ['nome_curso']


class EscolaridadeForm(ModelForm):
    class Meta:
        model = models.Escolaridade
        fields = ['titulo']


class EnderecoForm(ModelForm):
    class Meta:
        model = models.Endereco
        fields = ['cep', 'logradouro', 'numero', 'complemento',
                  'referencia', 'bairro', 'cidade', 'estado', 'pais', ]


class DepartamentoForm(ModelForm):
    class Meta:
        model = models.Departamento
        fields = ['nome', 'dataFundacao', 'diretor',
                  'quantidadeSalas', 'rendaAnual', 'cursos', ]


class CurriculoForm(ModelForm):
    class Meta:
        model = models.Curriculo
        fields = ['objetivo', 'pessoa', 'idLattes', 'pretensaoSalarial',
                  'ultimaAtualizacao', 'titulo', 'endereco', 'experiencia', 'competencias', 'formacoes', ]


class ArtigoForm(ModelForm):
    class Meta:
        model = models.Artigo
        fields = ['titulo', 'data', 'estudante',
                  'professor', 'resumo', 'paginas', 'nota', 'classificacao', 'apresentacao', 'disciplina', ]


class InstituicaoForm(ModelForm):
    class Meta:
        model = models.Instituicao
        fields = ['nome', 'cnpj', 'endereco',
                  'fundador', 'dataFundacao', 'site', 'telefone', 'numeroFuncionarios', 'departamentos', 'rendaAnual', ]


class LivroForm(ModelForm):
    class Meta:
        model = models.Livro
        fields = ['titulo', 'autores', 'editora',
                  'edicao', 'valor', 'dataCriacao', 'ano', 'disciplinas', 'estudante', 'emprestado', ]


class ProjetoPesquisaForm(ModelForm):
    class Meta:
        model = models.ProjetoDePesquisa
        fields = ['idLattes', 'titulo', 'inicio',
                  'fim', 'keywords', 'valorProjeto', 'situacao', 'alunos', 'professor', 'departamentoResponsavel', ]


class EstudanteForm(ModelForm):
    class Meta:
        model = models.Estudante
        fields = ['nome', 'nomeMae', 'dataNascimento', 'email', 'telefone', 'endereco', 'usuario', 'senha', 'cpf', 'rg',
                  'matricula', 'escolaridade', 'dataMatricula', 'dataColacao', 'usosRestauranteUniversitario', 'coeficienteRendimento', 'bolsista', 'bolsa', 'agenciaBancaria', 'contaBancaria']


class ProfessorForm(ModelForm):
    class Meta:
        model = models.Professor
        fields = [ 'nome', 'nomeMae', 'dataNascimento', 'email', 'telefone', 'endereco', 'usuario', 'senha', 'cpf', 'rg',
            'escolaridade', 'inscricao', 'dataAdmissao', 'interino', 'concursado', 'especialidade', 'salario', 'agenciaBancaria', 'contaBancaria', 'projetos']



class PessoaForm(ModelForm):
    class Meta:
        model = models.Pessoa
        fields = ['nome', 'nomeMae', 'dataNascimento', 'email', 'telefone', 'endereco', 'usuario', 'senha', 'cpf', 'rg']