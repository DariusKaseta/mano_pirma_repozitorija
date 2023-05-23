# Leistų įvesti darbuotojus: vardą, pavardę, gimimo datą, pareigas, atlyginimą, nuo kada dirba 
# (data būtų nustatoma automatiškai, pagal dabartinę datą).
# Duomenys būtų saugomi duomenų bazėję, panaudojant SQLAlchemy ORM (be SQL užklausų)
# Vartotojas galėtų įrašyti, peržiūrėti, ištrinti ir atnaujinti darbuotojus.

from datetime import datetime as dt
from darbuotoju_programa import Darbuotojas, engine, declarative_base, sessionmaker, create_engine

if __name__ == "__main__":
    engine = create_engine("sqlite:///darbuotoju_db.db", echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base = declarative_base()

    while True:
        pasirinkimas = int(input("""====Pasirinkite veiksma====: 
    1 - Darbuotojo ivedimas, 
    2 - Atnaujinimas, 
    3 - Trynimas,
    8 - Perziura, 
    9 - Iseiti>:"""))
        
        if pasirinkimas == 1:
            while True:
                try:
                    vardas = str(input("Iveskite varda:"))
                    pavarde = str(input("Iveskite pavarde:"))
                    gimimo_metai = dt.strptime(input("Iveskite gimimo metus (YYYY-MM-DD):"), "%Y-%m-%d").date()
                    pareigos = str(input("Iveskite uzimamas pareigas:"))
                    alga = float(input("Iveskite darbuotoja alga:"))
                    isidarbinimas = dt.now().date()
                    darbuotojas = Darbuotojas(vardas=vardas, pavarde=pavarde, gimimo_metai=gimimo_metai, 
                            pareigos=pareigos, alga=alga, isidarbinimas=isidarbinimas)
                    session.add(darbuotojas)
                    session.commit()
                    print("=======Darbuotojas sekmingai pridetas.=======")
                    break
    
                except ValueError as e:
                    print(f"=======Klaida:{e} Neteisingas ivedimas. Patikrinkite ivestus duomenis ir/ar formatus.=======")
    
                except Exception as e:
                    print(f"=======Klaida:{e} Programos klaida, bandykite dar karta.=======")
        
        
        elif pasirinkimas == 2:
            while True:
                try:
                    darbuotojo_id = int(input("=======Iveskite darbuotojo 'ID', kuris bus atnaujinamas:"))
                    darbuotojas = session.query(Darbuotojas).get(darbuotojo_id)
        
                    if darbuotojas:
                        try:
                            vardas = str(input("Iveskite nauja varda:"))
                            pavarde = str(input("Iveskite nauja pavarde:"))
                            gimimo_metai = dt.strptime(input("Iveskite naujus gimimo metus (YYYY-MM-DD):"), "%Y-%m-%d").date()
                            pareigos = str(input("Iveskite naujas uzimamas pareigas:"))
                            alga = float(input("Iveskite nauja darbuotojo alga:"))
                            isidarbinimas = dt.now().date()

                            darbuotojas.vardas = vardas
                            darbuotojas.pavarde = pavarde
                            darbuotojas.gimimo_metai = gimimo_metai
                            darbuotojas.pareigos = pareigos
                            darbuotojas.alga = alga
                            darbuotojas.isidarbinimas = isidarbinimas
                            session.add(darbuotojas)
                            session.commit()
                            print("=======Darbuotojas sekmingai atnaujintas.=======")
                            break
                                
                        except ValueError as e:
                            print(f"=======Klaida: {e}. atnaujinant darbuotojo duomenis.=======")
                        
                except TypeError as e:
                    print(f"=======Klaida: {e}. darbuotojas su nurodytu ID nerastas.=======")
                        
                except Exception as e:
                    print(f"=======Klaida: {e}. programos klaida, bandykite dar karta.=======")
                         

        elif pasirinkimas == 3:
            while True:
                try:
                    darbuotojo_id = int(input("=======Iveskite darbuotojo 'ID', kuris bus istrinamas:"))
                    darbuotojas = session.query(Darbuotojas).get(darbuotojo_id)

                    if darbuotojas:
                        session.delete(darbuotojas)
                        session.commit()
                        print("=======Darbuotojas sekmingai istrintas.=======")
                        break
                    else:
                        print("=======Darbuotojas su nurodytu ID nerastas.=======")
                        break
                    
                except ValueError as e:
                    print(f"=======Klaida: {e}. neteisingas ivedimas. Iveskite teisinga ID.=======")

        elif pasirinkimas == 8:
            while True:
                try:
                    darbuotojai = session.query(Darbuotojas).all()
                    if darbuotojai:
                        for darbuotojas in darbuotojai:
                            print(f"ID: {darbuotojas.id}")
                            print(f"Vardas: {darbuotojas.vardas}")
                            print(f"Pavarde: {darbuotojas.pavarde}")
                            print(f"Gimimo metai: {darbuotojas.gimimo_metai}")
                            print(f"Pareigos: {darbuotojas.pareigos}")
                            print(f"Atlyginimas: {darbuotojas.alga}")
                            print(f"Isidarbinimo data: {darbuotojas.isidarbinimas}")
                            print("----------------------------")
                        break
                    else:
                        print("=======Nerasta jokiu duomenu.=======")
                        break
                except Exception as e:
                    print(f"=======Klaida: {e}. Programos klaida, bandykite dar karta.=======")
                    break

        elif pasirinkimas == 9:
            print("======= PROGRAMOS PABAIGA=======")
            break







