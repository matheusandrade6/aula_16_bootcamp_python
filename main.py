from typing import Optional
from sqlmodel import Field, SQLModel, Session, create_engine

class Hero(SQLModel, table=True): #Table=True mostra pra classe que isso é uma tabela em um banco de dados
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None

hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)


engine = create_engine("sqlite:///database.db", echo=True) 

#cria o db no SGBD, no caso SQLite
SQLModel.metadata.create_all(engine)

#Insert no db criado
with Session(engine) as session:
    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)
    session.commit()