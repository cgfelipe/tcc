# Generated by Django 2.1 on 2018-11-09 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180924_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='dataNascimento',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='endereco',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Endereco', verbose_name='endereço da pessoa'),
        ),
    ]
