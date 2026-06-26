class Pessoa:
    def __init__(self, telefone, email):
        self.telefone = telefone
        self.email = email

    def exibir_dados(self):
        print(f"Telefone: {self.telefone}")
        print(f"Email: {self.email}")


class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf, telefone, email):
        self.nome = nome
        self.cpf = cpf
        super().__init__(telefone, email)

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        super().exibir_dados()


class PessoaJuridica(Pessoa):
    def __init__(self, nome_fantasia, cnpj, telefone, email):
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        super().__init__(telefone, email)

    def exibir_dados(self):
        print(f"Nome Fantasia: {self.nome_fantasia}")
        print(f"CNPJ: {self.cnpj}")
        super().exibir_dados()