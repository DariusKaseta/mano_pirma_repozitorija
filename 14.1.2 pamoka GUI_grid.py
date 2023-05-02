import PySimpleGUI as sg

layout = [[sg.Text("Vardas"), sg.Input(key="vardas", size=20)],
          [sg.Text("Pavarde"), sg.Input(key="pavarde", size=20)],
          [sg.Text("Gimimo data"), sg.Input(key="metai", size=5), sg.Input(key="menuo", size=3), sg.Input(key="diena", size=3)],
          
          
          [sg.Button("Patvirtinti")],
          [sg.Text(key="confirmation")],]  
          

window = sg.Window("Pavyzdys", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    window ['confirmation'].update(
        f"{values['vardas']}-{values['pavarde']} gime " + \
        f"{values['metai']}-{values['menuo']}-{values['diena']}"
    )

window.close()