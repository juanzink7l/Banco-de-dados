import os

from models import Curso, Turma, Professor, Aluno


def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    curso = Curso(id_curso="", curso="")
    turma = Turma(codigo_turma="", turma="", carga_horaria="", numero_alunos="")
    professor = Professor(matricula_professor="", nome="", email="")
    aluno = Aluno(matricula_aluno="", nome="", cpf="", email="")

    limpar()

#Entrada de informaçoes sobre o curso
    curso.id_curso = input("Informe o ID do seu curso: ").strip()
    curso.curso = input("Informe o seu curso: ").strip()

    limpar()

#Entrada de informaçoes sobre a turma   
    turma.codigo_turma = input("Informe o código da turma: ").strip()
    turma.turma = input("Informe sua turma: ").strip()
    turma.carga_horaria = input("Informe a carga horária do curso:").strip()
    turma.numero_alunos = input(" Informe a quantidade de alunos: ").strip()







