# Generated by Django 2.1.1 on 2018-09-21 19:28
# Generated by Django 2.0.3 on 2018-09-24 15:13

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('data', models.DateField()),
                ('resumo', models.CharField(max_length=500)),
                ('paginas', models.IntegerField()),
                ('nota', models.FloatField()),
                ('classificacao', models.CharField(max_length=10)),
                ('apresentacao', models.BooleanField()),
                ('disciplina', models.CharField(max_length=30)),
            ],
            bases=(core.models.Base, models.Model),
        ),
        migrations.CreateModel(
            name='Curriculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objetivo', models.CharField(max_length=500)),
                ('idLattes', models.CharField(max_length=10)),
                ('pretensaoSalarial', models.FloatField()),
                ('ultimaAtualizacao', models.DateField()),
                ('titulo', models.CharField(max_length=30)),
                ('experiencia', models.CharField(max_length=500)),
                ('competencias', models.CharField(max_length=500)),
                ('formacoes', models.CharField(max_length=500)),
            ],
            bases=(core.models.Base, models.Model),
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('dataFundacao', models.DateField()),
                ('quantidadeSalas', models.IntegerField()),
                ('rendaAnual', models.FloatField()),
                ('cursos', models.ManyToManyField(to='core.Curso')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=10)),
                ('logradouro', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=10)),
                ('complemento', models.CharField(max_length=50)),
                ('referencia', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=30)),
                ('cidade', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=2)),
                ('pais', models.CharField(max_length=30)),
            ],
            bases=(core.models.Base, models.Model),
        ),
        migrations.CreateModel(
            name='Escolaridade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('nome', models.CharField(max_length=200)),
                ('cnpj', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('dataFundacao', models.DateField()),
                ('site', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=200)),
                ('numeroFuncionarios', models.IntegerField()),
                ('rendaAnual', models.FloatField()),
                ('departamentos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Departamento', verbose_name='lista de departamentos')),
                ('endereco', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Endereco', verbose_name='endereço da instituição')),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('autores', models.CharField(max_length=200)),
                ('editora', models.CharField(max_length=200)),
                ('edicao', models.IntegerField()),
                ('valor', models.FloatField()),
                ('dataCriacao', models.DateField()),
                ('ano', models.IntegerField()),
                ('disciplinas', models.CharField(max_length=200)),
                ('emprestado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('nome', models.CharField(max_length=200)),
                ('nomeMae', models.CharField(max_length=200)),
                ('dataNascimento', models.DateField()),
                ('email', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=30)),
                ('usuario', models.CharField(max_length=20)),
                ('senha', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('rg', models.CharField(max_length=8)),
            ],
            bases=(core.models.Base, models.Model),
        ),
        migrations.CreateModel(
            name='ProjetoDePesquisa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idLattes', models.CharField(max_length=100)),
                ('titulo', models.CharField(max_length=200)),
                ('inicio', models.DateField()),
                ('fim', models.DateField()),
                ('keywords', models.CharField(max_length=200)),
                ('valorProjeto', models.FloatField()),
                ('situacao', models.CharField(max_length=200)),
                ('alunos', models.CharField(max_length=200)),
                ('departamentoResponsavel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Departamento', verbose_name='departamento responsavel')),
            ],
        ),
        migrations.CreateModel(
            name='Estudante',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core.Pessoa')),
                ('matricula', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('dataMatricula', models.DateField()),
                ('dataColacao', models.DateField()),
                ('usosRestauranteUniversitario', models.IntegerField()),
                ('coeficienteRendimento', models.FloatField()),
                ('bolsista', models.BooleanField()),
                ('bolsa', models.FloatField()),
                ('agenciaBancaria', models.CharField(max_length=200)),
                ('contaBancaria', models.CharField(max_length=200)),
                ('escolaridade', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Escolaridade', verbose_name='escolaridade do aluno')),
            ],
            bases=('core.pessoa',),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Pessoa')),
                ('inscricao', models.CharField(max_length=10)),
                ('dataAdmissao', models.DateField()),
                ('interino', models.BooleanField()),
                ('concursado', models.BooleanField()),
                ('salario', models.FloatField()),
                ('agenciaBancaria', models.CharField(max_length=200)),
                ('contaBancaria', models.CharField(max_length=200)),
                ('projetos', models.CharField(max_length=500)),
                ('escolaridade', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Escolaridade', verbose_name='escolaridade do professor')),
                ('especialidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Especialidade', verbose_name='especialidades do professor')),
            ],
            bases=('core.pessoa',),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='endereco',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Endereco', verbose_name='endereço da pessoa'),
        ),
        migrations.AddField(
            model_name='instituicao',
            name='fundador',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Pessoa', verbose_name='fundador da instituição'),
        ),
        migrations.AddField(
            model_name='curriculo',
            name='endereco',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Endereco', verbose_name='endereco do curriculo'),
        ),
        migrations.AddField(
            model_name='curriculo',
            name='pessoa',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Pessoa', verbose_name='responsavel do curriculo'),
        ),
        migrations.AddField(
            model_name='projetodepesquisa',
            name='professor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Professor', verbose_name='professor orientador'),
        ),
        migrations.AddField(
            model_name='livro',
            name='estudante',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Estudante', verbose_name='estudante que usa o livro'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='diretor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Professor', verbose_name='diretor do departamento'),
        ),
        migrations.AddField(
            model_name='artigo',
            name='estudante',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Estudante', verbose_name='estudante responsavel'),
        ),
        migrations.AddField(
            model_name='artigo',
            name='professor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Professor', verbose_name='professor orientador'),
        ),
    ]
