#cria a classe pessoa
class Pessoa:
    #construtor da classe
    def __init__(self, id_pessoa, nome, cpf, email):

        self.id_pessoa = id_pessoa
        self.nome = nome
        self.cpf = cpf
        self.email = email

    def cartao_visitas(self):
        print(f"\n{'-'*20} DADOS DO USUARIO {'-' *20}\n")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Email: {self.email}")

    def apresentar(self):
        return f"olá meu nome nao é {self.nome}, meu cpf nao é {self.cpf} e meu email nao é {self.email} e meu identificador nao é {self.id_pessoa}."
#programa principal
def main():
    #instancia a classe
    usuario = Pessoa(1, "null", "null", "null")

    #dar valores aos atributos
    usuario.nome = input("informe seu nome:").strip().title()
    usuario.cpf = input("informe seu cpf:").strip()
    usuario.email = input("informe seu email:").strip()

# exibe os atributos do objeto usuario
    print(usuario.apresentar())
    usuario.cartao_visitas()

if __name__ == "__main__":
    main()









