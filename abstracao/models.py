from abc import ABC, abstractmethod

#classe abstrata
class lConta(ABC): 
    @abstractmethod
    def consultar_saldo(self):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

#class conta
class Conta(lConta):
    def __init__(self, titular, cpf, agencia, n_conta, saldo):
        self.titular = titular
        self.cpf = cpf
        self.agencia = agencia
        self.n_conta = n_conta
        self.saldo = saldo
        
    def consultar_saldo(self):
        print(f"Nome do titular: {self.titular}")
        print(f"CPF do titular: {self.cpf}")
        print(f"Agencia: {self.agencia}")
        print(f"Conta: {self.n_conta}")
        print(f"Saldo da conta: R$ {self.saldo:.2f}")

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def sacar(self, valor):
        self.saldo -= valor 
        return self.saldo