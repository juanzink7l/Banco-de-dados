import os

from models import Veiculo

def main():
    carro = Veiculo("null", "null", "null", "null", "null")

    carro.fabricante = input("Digite o seu nome: ").strip().title()
    carro.modelo = input("Digite o modelo do seu carro: ").strip().title()
    carro.cor = input("Digite a cor do seu carro: ").strip()
    carro.ano = input("Digite o ano do seu carro: ").strip()
    carro.placa = input("Digite a placa de seu carro: ").strip().upper()

    carro.exibir_dados()

if __name__ == "__main__":
    main()