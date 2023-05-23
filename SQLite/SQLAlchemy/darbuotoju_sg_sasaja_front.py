# Perdaryti programą 1 užduotyje, kad ji:

# Turėtų grafinę sąsają (su ikona ir pavadinimu). Sukurti per Gui
# Leistų įvesti asmenis į duomenų bazę (jų vardą, pavardę, amžių, ...)
# Parodytų visų į duomenų bazę įvestų asmenų sąrašą
# Leistų ištrinti pasirinktą asmenį iš duomenų bazės
# Leistų paredaguoti įvesto asmens duomenis ir įrašyti atnaujinimus į duomenų bazę.
# Sukurti paleidžiamąjį programos failą (exe, su ikona)

from datetime import datetime as dt
import PySimpleGUI as sg
from darbuotoju_sg_sasaja_back import Darbuotojas, engine, sessionmaker, create_engine, declarative_base


engine = create_engine("sqlite:///darbuotoju_db.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

if __name__ == "__main__":

    class DarbuotojasGui:
        def __init__(self):
            self.layout = [
                [sg.Text("Darbuotojo vardas:"), sg.Input(key="vardas")],
                [sg.Text("Darbuotojo pavarde:"), sg.Input(key="pavarde")],
                [sg.Text("Irasykite darbuotojo gimimo metus (YYYY-MM-DD):"), sg.Input(key="gimimo_metai")],
                [sg.Text("Darbuotojo pareigos:"), sg.Input(key="pareigos")],
                [sg.Text("Darbuotojo alga:"), sg.Input(key="alga")],
                [sg.Text("Kada pradeda dirbti:"), sg.Input(default_text=dt.now().strftime("%Y-%m-%d %H:%M:%S"), key="isidarbinimas")],
                [sg.Button("Ivesti"), sg.Button("Parodyti sarasa"), sg.Button("Redaguoti"), sg.Button("Iseiti")]
            ]
            self.window = sg.Window("Darbuotoju programa", self.layout)


        def run(self):
            while True:
                event, values = self.window.read()
                if event == "Iseiti" or event == sg.WINDOW_CLOSED:
                    break
                if event == "Ivesti":
                     self.ivesti_duomenis(values)
                elif event == "Parodyti sarasa":
                    self.parodyti_sarasa()
                elif event == "Redaguoti":
                    self.redaguoti_sarasa()

            self.window.close
            

        def ivesti_duomenis(self, values):
            vardas = values["vardas"]
            pavarde = values["pavarde"]
            gimimo_metai = dt.strptime(values["gimimo_metai"], "%Y-%m-%d").date()
            pareigos = values["pareigos"]
            alga = float(values["alga"])
            dirba_nuo = dt.strptime(values["isidarbinimas"].split()[0], "%Y-%m-%d").date()

            darbuotojas = Darbuotojas(vardas=vardas, pavarde=pavarde, gimimo_metai=gimimo_metai,pareigos=pareigos,
                                      alga=alga,dirba_nuo=dirba_nuo)
            session.add(darbuotojas)
            session.commit()
            sg.popup("Darbuotojas sekmingai pridetas")


        def parodyti_sarasa(self):
            darbuotojai = session.query(Darbuotojas).all()
            darbuotojai_list = [f"{darbuotojas.vardas} {darbuotojas.pavarde} {darbuotojas.gimimo_metai} {darbuotojas.pareigos} {darbuotojas.alga} {darbuotojas.dirba_nuo}" 
                                for darbuotojas in darbuotojai if darbuotojas.vardas and darbuotojas.pavarde]
            if darbuotojai_list:
                sg.popup(f"Viso darbuotoju: {len(darbuotojai_list)}")
                layout = [
                    [sg.Table(values=darbuotojai_list,
                              headings=["Vardas", "Pavarde", "Gimimo metai", "Pareigos", "Alga", "Dirba nuo"],
                            #   auto_size_columns=True, 
                            #   justification="left", 
                              num_rows=min(100, len(darbuotojai_list)))]]
                
                window = sg.Window("Darbuotoju sarasas", layout)
                while True:
                    event, values = window.read()
                    if event == sg.WIN_CLOSED:
                        break
                window.close()
            else:
                sg.popup("Darbuotoju nera bazeje.")
                    

        def redaguoti_sarasa(self):
            darbuotojai = session.query(Darbuotojas).all()
            darbuotojai_list = [f"{darbuotojas.vardas} {darbuotojas.pavarde}" for darbuotojas in darbuotojai]
            if darbuotojai_list:
                layout = [
                    [sg.Text("Pasirinkite darbuotoja:", size=(30,5))],
                    [sg.Listbox(values=darbuotojai_list, size=(30,5), key="saraso_elementai")],
                    [sg.Button("Redaguoti"), sg.Button("Istrinti")]]
                window = sg.Window("Redaguoti darbuotoja", layout)
                event, values = window.read()
                window.close()
                
                
                if event == "Redaguoti":
                    pasirinktas = values["saraso_elementai"]
                    if not pasirinktas:
                        sg.popup("Pasirinkite darbuotoja, kuri norite redaguoti.") 
                    else:    
                        pasirinktas = pasirinktas[0]
                        vardas, pavarde = pasirinktas.split()
                        darbuotojas = session.query(Darbuotojas).filter_by(vardas=vardas, pavarde=pavarde).first() if vardas and pavarde else None
                    
                        if darbuotojas:
                            layout = [
                                [sg.Text(f"Darbuotojo vardas:"),
                                sg.Input(key="vardas", default_text=darbuotojas.vardas)],
                                
                                [sg.Text(f"Darbuotojo pavarde:"),
                                sg.Input(key="pavarde", default_text=darbuotojas.pavarde)],
                                
                                [sg.Text(f"Darbuotojo gimimo metai:"),
                                sg.Input(key="gimimo_metai", default_text=darbuotojas.gimimo_metai)],
                                    
                                [sg.Text(f"Darbuotojo pareigos:"),
                                sg.Input(key="pareigos", default_text=darbuotojas.pareigos)],
                                    
                                [sg.Text(f"Darbuotojo alga:"),
                                sg.Input(key="alga", default_text=darbuotojas.alga)],
                                
                                [sg.Text(f"Kada pradeda dirbti:"),
                                sg.Input(key="isidarbinimas", default_text=darbuotojas.dirba_nuo)],
                                    
                                [sg.Button("Atnaujinti")]]
                        
                        window = sg.Window("Redaguoti darbuotoja", layout)
                        event, values = window.read()
                        window.close()
                
                    if event == "Atnaujinti":
                        darbuotojas.vardas = values["vardas"]
                        darbuotojas.pavarde = values["pavarde"]
                        darbuotojas.gimimo_metai = dt.strptime(values["gimimo_metai"], "%Y-%m-%d").date()
                        darbuotojas.pareigos = values["pareigos"]
                        darbuotojas.alga = values["alga"]
                        darbuotojas.dirba_nuo = dt.strptime(values["isidarbinimas"], "%Y-%m-%d").date()
                        session.commit()
                        sg.popup("Darbuotojo duomenys atnaujinti.")

                elif event == "Istrinti":
                    pasirinktas = values["saraso_elementai"]
                    if not pasirinktas:
                        sg.popup("Pasirinkite darbuotoja, kuri norite istrinti.")
                    
                    else:
                        pasirinktas = pasirinktas[0]
                        vardas, pavarde = pasirinktas.split()
                        darbuotojas = session.query(Darbuotojas).filter_by(vardas=vardas, pavarde=pavarde).first() if vardas and pavarde else None
                        if darbuotojas:
                            layout = [
                                    [sg.Text("Ar tikrai norite istrinti pasirinkta darbuotoja?")],
                                    [sg.Button("Taip"), sg.Button("Ne")]]

                            window = sg.Window("Patvirtinimas", layout)
                            event, _ = window.read()
                            window.close()

                            if event == "Taip":
                                session.delete(darbuotojas)
                                session.commit()
                                sg.popup("Darbuotojas sekmingai istrintas")
                            else:
                                sg.popup("Pasirinktas darbuotojas atmestas.")
            else:
                sg.popup("Darbuotoju sarasas yra tuscias.")

darbuotojas_gui = DarbuotojasGui()
darbuotojas_gui.run()

        