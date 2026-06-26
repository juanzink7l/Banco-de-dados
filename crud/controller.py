import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def cadastrar(session, Pessoa):
    try:
        nome = input("Informe o nome: ").strip().title()
        cpf = input("Informe o CPF: ").strip()
        email = input("Informe o Email: ").strip().lower()

        pessoasCpf = session.query(Pessoa).filter(Pessoa.cpf.like(cpf)).all()
        pessoasEmail = session.query(Pessoa).filter(Pessoa.email.like(email)).all()

        if cpf in [pessoa.cpf for pessoa in pessoasCpf]:
            return "CPF ja cadastrado."
        elif email in [pessoa.email for pessoa in pessoasEmail]:
            return "Email já cadastrado."
        else:
            nova_pessoa = Pessoa(nome=nome, cpf=cpf, email=email)

            session.add(nova_pessoa)
            session.commit()

        return f"{nova_pessoa} cadastrado com sucesso."
    except Exception as e:
        print(f"Não foi possivel cadastrar.")

def listar(session, Pessoa):
    try:
        pessoas = session.query(Pessoa).all()

        print(f"Pessoas cadastradas: \n")
        for pessoa in pessoas:
            print(f"ID: {pessoa.id_pessoa}")
            print(f"Nome: {pessoa.nome}")
            print(f"CPF: {pessoa.cpf}")
            print(f"Email: {pessoa.email}")
            print(f"\n {'-'*100}\n")
    except Exception as e:
        print(f"Não foi possivel listar. {e}")

def atualizar(session, Pessoa):
    id_pessoa = ""
    nome = ""
    cpf = ""
    email = ""

    try:
        print("Escolha o campo que deseja pesquisar: ")
        print("1 - ID")
        print("2 - CPF")
        print("3 - Email")
        print("4 - Retornar")
        
        pesquisar = input("Qaul o campo desejado? ").strip()

        limpar()

        match pesquisar:
            case "1":
                id_pessoa = input("Informe pelo o ID a pesquisar").strip()
                pessoa = session.query(Pessoa).filter_by(id_pessoa=id_pessoa).first()
            case "2":
                CPF = input("Informe pelo o CPF a pesquisar").strip()
                pessoa = session.query(Pessoa).filter_by(cpf=cpf).first()
            case "3":
                email = input("Informe pelo o email a pesquisar").strip()
                pessoa = session.query(Pessoa).filter_by(email=email).first()
            case "4":
                return ""
            case _:
                return "Opção inválida."
            
        if pessoa:
            limpar()

            while True:
                print(f"ID: {pessoa.id_pessoa}")
                print("Qual o campo deseja alterar?")
                print(f"1 - Nome: {pessoa.nome}")
                print(f"1 - CPF: {pessoa.cpf}")
                print(f"1 - Email: {pessoa.email}")
    except Exception as e:
        print(f"Não foi possível alterar os dados. {e}")

    