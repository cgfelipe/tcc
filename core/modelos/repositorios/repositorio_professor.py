from core.modelos.repositorios.base_repositorio import BaseRepositorio
from core.modelos.entidades.Professor import Professor


class RepositorioProfessor(BaseRepositorio):
    def cadastrar(self, professor: Professor):
        return professor.save()

    def buscar(self, cpf):
        return Professor.objects.get(cpf=cpf)

    def listar_todos(self):
        return Professor.objects.all()

    def atualizar(self, cpf, **kwargs):
        modifiers = dict(**kwargs)
        for k, v in kwargs.items():
            if not hasattr(Professor, k):
                del modifiers[k]
        professor = Professor.objects.filter(cpf=cpf)
        professor.update(**modifiers)
        return professor.first()

    def remover(self, **kwargs):
        professor = Professor.objects.get(**kwargs)
        if professor:
            professor.delete()
