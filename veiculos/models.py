class Veiculo:
    def __init__(self, fabricante, modelo, cor, ano, placa):
        self.fabricante = fabricante
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.placa = placa

    def exibir_dados(self):
        print(f"Fabricante: {self.fabricante}")
        print(f"modelo: {self.modelo}")
        print(f"cor: {self.cor}")
        print(f"ano: {self.ano}")
        print(f"placa: {self.placa}")