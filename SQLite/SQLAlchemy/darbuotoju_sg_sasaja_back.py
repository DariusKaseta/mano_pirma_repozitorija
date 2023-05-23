# Perdaryti programą 1 užduotyje, kad ji:

# Turėtų grafinę sąsają (su ikona ir pavadinimu). Sukurti per Gui
# Leistų įvesti asmenis į duomenų bazę (jų vardą, pavardę, amžių, ...)
# Parodytų visų į duomenų bazę įvestų asmenų sąrašą
# Leistų ištrinti pasirinktą asmenį iš duomenų bazės
# Leistų paredaguoti įvesto asmens duomenis ir įrašyti atnaujinimus į duomenų bazę.
# Sukurti paleidžiamąjį programos failą (exe, su ikona)

from sqlalchemy import Integer, String, Float, Column, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///darbuotoju_db.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Darbuotojas(Base):
    __tablename__ = "Darbuotojas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    vardas = Column("Vardas", String(50), nullable=False)
    pavarde = Column("Pavarde", String(50), nullable=False)
    gimimo_metai = Column("Gimimo metai", Date, nullable=False)
    pareigos = Column("Pareigos", String(50), nullable=False)
    alga = Column("Alga", Float, nullable=False)
    dirba_nuo = Column("Dirba nuo", Date)

    def __init__ (self, vardas, pavarde, gimimo_metai, pareigos, alga, dirba_nuo, id=None):
        self.id = id
        self.vardas = vardas
        self.pavarde = pavarde
        self.gimimo_metai = gimimo_metai
        self.pareigos = pareigos
        self.alga = alga
        self.dirba_nuo = dirba_nuo

    def __repr__ (self):
        return f"{self.id}, {self.vardas}, {self.pavarde}, {self.gimimo_metai}, {self.pareigos}, {self.pareigos}, {self.alga}, {self.dirba_nuo}"
    
Base.metadata.create_all(engine)
    
    