from sqlalchemy import Column, String, Integer

def criar_tb_pessoa(engine, Base):
    try: 
        class Pessoa(Base):
            __tablename__ = "pessoa" 

            #atributos
            id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
            nome = Column(String, nullable=False)
            cpf = Column(String, nullable=False, unique=True)
            email = Column(String, nullable=False, unique=True)

            def __str__(self):
                return self.nome

        Base.metadata.create_all(engine)

        return Pessoa
    except Exception as e:
        print(f"Não foi possível conectar com o Banco de Dados. {e}")