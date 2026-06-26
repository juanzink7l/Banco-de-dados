class Curso:
    def __init__(self, id_curso, curso):
        self.id_curso = id_curso
        self.curso = curso

    def exibir_dados(self):
        print(f"Curso: {self.curso}")
        print(f"ID curso: {self.id_curso}")

class Turma:
    def __init__(self, codigo_turma, turma, carga_horaria, numero_alunos):
        self.codigo_turma = codigo_turma
        self.turma = turma
        self.carga_horaria = carga_horaria
        self.numero_alunos = numero_alunos
    
    def exibir_dados(self):
        print(f"Código da turma: {self.codigo_turma}")
        print(f"Turma: {self.turma}")
        print(f"Carga horária: {self.carga_horaria}")
        print(f"Quantidade de alunos: {self.numero_alunos}")

class Professor:
    def __init__(self, matricula_professor, nome, email):
        self.matricula_professor = matricula_professor
        self.nome = nome
        self.email = email
       
    def exibir_dados(self):
        print(f"Matricula do Professor: {self.matricula_professor}")
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")

class Aluno:
    def __init__(self, matricula_aluno, nome, cpf, email):
        self.matricula_aluno = matricula_aluno
        self.nome = nome
        self.cpf = cpf
        self.email = email

    def exibir_dados(self):
        print(f"Matrícula do aluno: {self.matricula_aluno}")
        print(f"Nome do aluno: {self.nome}")
        print(f"CPF do aluno: {self.cpf}")
        print(f"Email: {self.email}")
