import pandas as pd

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
    cpf = ""
    email = ""
    novo_nome = ""
    novo_cpf = ""
    novo_email = ""

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
                id_pessoa = input("Informe pelo o ID a pesquisar: ").strip()
                pessoa = session.query(Pessoa).filter_by(id_pessoa=id_pessoa).first()
            case "2":
                cpf = input("Informe pelo o CPF a pesquisar: ").strip()
                pessoa = session.query(Pessoa).filter_by(cpf=cpf).first()
            case "3":
                email = input("Informe pelo o email a pesquisar: ").strip()
                pessoa = session.query(Pessoa).filter_by(email=email).first()
            case "4":
                return ""
            case _:
                return "Opção inválida."
            
        if pessoa:
            limpar()

            while True:
                print(f"ID: {pessoa.id_pessoa}")
                print("Qual campo deseja alterar?  ")
                print(f"1 - Nome: {pessoa.nome}")
                print(f"2 - CPF: {pessoa.cpf}")
                print(f"3 - Email: {pessoa.email}")
                print("4 - Finalizar as alterações")

                campo = input("Campo desejado: ").strip()

                limpar()

                match campo:
                    case "1":
                        novo_nome = input("Informe o novo nome: ").strip().title()
                        continue
                    case "2":
                        novo_cpf = input("Informe o novo CPF: ").strip()
                        pessoas = session.query(Pessoa).filter(Pessoa.cpf == novo_cpf).all()
                        if novo_cpf in [pessoa.cpf for pessoa in pessoas]:
                            print("CPF já cadastrado.")
                            continue
                    case "3":
                        novo_email = input("Informe o novo email: ").strip().lower()
                        pessoas = session.query(Pessoa).filter(Pessoa.email == novo_email).all()
                        if novo_email in [pessoa.email for pessoa in pessoas]:
                            print("Email já cadastrado.")
                            continue
                    case "4":
                        novo_nome = novo_nome if novo_nome != "" else pessoa.nome
                        novo_cpf = novo_cpf if novo_cpf != "" else pessoa.cpf
                        novo_email = novo_email if novo_email != "" else pessoa.email
                        break
                    case _:
                        print("Campo inexistente.")
                        continue

            pessoa.nome = novo_nome
            pessoa.cpf = novo_cpf
            pessoa.email = novo_email

            session.commit()

            return "Dados atualizados com sucesso."
    except Exception as e:
        print(f"Não foi possível alterar os dados. {e}")

def deletar(session, Pessoa):
    id_pessoa = ""
    cpf = ""
    email = ""
    
    print("Informe o campoo que deseja pesquisar: ")
    print("1 - ID")
    print("2 - CPF")
    print("3 - Email")
    print("4 - Retornar")

    opcao = input("Qual campo deseja pesquisar? ").strip()

    limpar()

    match opcao:
        case "1":
            id_pessoa = input("Informe o ID da pessoa que deseja excluir: ").strip()
            pessoa = session.query(Pessoa).filter_by(id_pessoa=id_pessoa).first()
        case "2":
            cpf = input("Informe o CPF da pessoa que deseja excluir: ").strip()
            pessoa = session.query(Pessoa).filter_by(cpf=cpf).first()
        case "3":
            email = input("Informe o Email da pessoa que deseja excluir: ").strip().lower()
            pessoa = session.query(Pessoa).filter_by(email=email).first()
        case _:
            return "Opção inválida."
        
    if pessoa: 
        limpar()
        print(f"ID: {pessoa.id_pessoa}")
        print(f"Nome: {pessoa.nome}")
        print(f"CPF: {pessoa.cpf}")
        print(f"Email: {pessoa.email}")
        print(f"\nDeseja excluir essa pessoa? \n")
        print("1 - Sim")
        print("2 - Não")
        confirmar = input("Informe o que deseja fazer: ").strip()

        limpar()

        match confirmar:
            case "1":
                session.delete(pessoa)
                session.commit()
                return "Pessoa excluída com sucesso"
            case "2":
                return ""
            case _:
                return "Opção inválida."
            
def exportar_excel(session, Pessoa):
    try:
        pessoas = session.query(Pessoa).all()

        dados =[
            {
                "ID": pessoa.id_pessoa,
                "Nome": pessoa.nome,
                "CPF": pessoa.cpf,
                "Email": pessoa.email
            }
            for pessoa in pessoas
        ]
    
        df = pd.DataFrame(dados)
        xlsx = input("Informe o nome do arquivo: ").strip()
        df.to_excel(f"crud/planilhas_exportadas/{xlsx}.xlsx", index=False)

        return f"Dados exportados para {xlsx}.xlsx com sucesso."
    except Exception as e:
        return f"Erro ao exportar dados. {e}."