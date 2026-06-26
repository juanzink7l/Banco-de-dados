import os 

from models import Conta

def limpar(): 
    os.system("cls" if os.name == "nt" else "clear")

def main():
    cc = Conta(titular="", cpf="", agencia="", n_conta="", saldo=0.0)

    limpar()

    cc.titular = input("Informe o nome do titular da conta:").strip().title()
    cc.cpf = input("informe o CPF do titular da conta: ").strip()

    limpar()

    while True:
        #exibir menu de opçoes
        print("1 - Consultar saldo da conta")
        print("2 - Depositar valor na conta")
        print("3 - Sacar valor da conta")
        print("4 - Sair do programa")
        opcao = input("Escolha a opçao desejada: ").strip()

        limpar()

        match opcao:
            case "1":
                cc.consultar_saldo()
                continue
            case "2":
                valor = float(input("Informe o valor do depósito: R$").replace(",", "."))
                if valor > 0:
                    print(f"Depósito efetuado com sucesso!")
                    print(f"Valor do depósito: R$ {cc.depositar(valor):.2f}")
                else:
                    print("Valor do depósito inválido")
                continue
            case "3":
                valor = float(input("Informe o valor do saque: R$").replace(",", "."))
                if valor > 0:
                    if cc.saldo > valor:
                        print("Saque efetuado com sucesso")
                        print(f"Saldo atual: R$ {cc.sacar(valor):.2f}")
                    else:
                        print("Saldo insuficiente")
                else:
                    print("Valor do saque é inválido")
            case "4":
                print("Programa encerrado")
                break
            case "_":
                print("Opçao invalida")
                continue

if __name__ == "__main__":
    main()