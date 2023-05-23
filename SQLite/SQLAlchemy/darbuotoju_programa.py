from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from typing import Any

engine = create_engine("sqlite:///darbuotoju_db.db", echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Darbuotojas(Base):
    __tablename__ = "Darbuotojai"
    id = Column(Integer, primary_key=True)
    vardas = Column("vardas:", String(50), nullable=False)
    pavarde = Column("pavarde:", String(50), nullable=False)
    gimimo_metai = Column("gimimo metai:(YYYY-MM-DD)", Date, nullable=False)
    pareigos = Column("uzimamos pareigos:", String(50), nullable=True)
    alga = Column("atlyginimas:", Float, nullable=False)
    isidarbinimas = Column("dirba nuo:", Date, nullable=False)

    def __init__(self, **kw: Any):
        # super().__init__(**kw)
        for key, value in kw.items():
            setattr(self, key, value)

    def __repr__(self) -> str:
        return f"({self.id}, {self.vardas}, {self.pavarde}, {self.gimimo_metai}, {self.pareigos}, {self.alga}, {self.isidarbinimas})"


def spausdinti(session):
    projektai = session.query(Darbuotojas).all()
    print("------------------")
    for projektas in projektai:
        print(projektas)
    print("------------------")
    return projektai

Base.metadata.create_all(engine)