import os

from models import PessoaFisica, PessoaJuridica


def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    # Instancia os objetos
    usuario = PessoaFisica(nome="", cpf="", telefone="", email="")
    empresa = PessoaJuridica(nome_fantasia="", cnpj="", telefone="", email="")

    limpar()

    # Entrada de dados do usuário
    usuario.nome = input("Informe o nome do usuário: ").strip().title()
    usuario.cpf = input("Informe o CPF do usuário: ").strip()
    usuario.email = input("Informe o e-mail do usuário: ").strip().lower()
    usuario.telefone = input("Informe o telefone do usuário: ").strip()

    limpar()

    # Entrada de dados da empresa
    empresa.nome_fantasia = input("Informe o nome da empresa: ").strip().title()
    empresa.cnpj = input("Informe o CNPJ da empresa: ").strip()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()
    empresa.email = input("Informe o e-mail da empresa: ").strip().lower()

    limpar()

    # Exibe os dados
    print(f"{'-'*20} DADOS DO USUÁRIO {'-'*20}")
    usuario.exibir_dados()

    print()

    print(f"{'-'*20} DADOS DA EMPRESA {'-'*20}")
    empresa.exibir_dados()


if __name__ == "__main__":
    main()