from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from models import criar_tb_pessoa
from controller import limpar, cadastrar, listar 

def main():
    base_dir = Path(__file__).resolve().parent
    db_dir = base_dir / "database"
    db_dir.mkdir(parents=True, exist_ok=True)

    db_path = db_dir / "db_crud.db"
    engine = create_engine(f"sqlite:///{db_path}")
    Base = declarative_base()
    Pessoa = criar_tb_pessoa(engine, Base)
    Session = sessionmaker(bind=engine)
    session = Session()

    limpar()

    while True:
        #menu
        print("0 - Sair do programa")
        print("1 - Cadastrar nova pessoa")
        print("2 - Listar pessoas")

        opcao = input("Informe a opçao desejada: ").strip()

        limpar()

        match opcao:
            case "0":
                print("Programa encerrado")
                break
            case "1":
                print(cadastrar(session, Pessoa))
                continue
            case "2":
                listar(session, Pessoa)
                continue
            case _:
                print("Opçao inválida")
                continue
            
if __name__ ==  "__main__":
    main()