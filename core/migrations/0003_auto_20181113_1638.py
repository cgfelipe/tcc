# Generated by Django 2.1.2 on 2018-11-13 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20181113_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projetodepesquisa',
            name='departamentoResponsavel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Departamento', verbose_name='departamento responsavel'),
        ),
        migrations.AlterField(
            model_name='projetodepesquisa',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Professor', verbose_name='professor orientador'),
        ),
    ]
