
def greitis():
    
    x = float(input('Įveskite greitį:'))
    
    if x <= 50.0 and x <= 53.0:
        return (x, 'leistinas greitis')
    elif x > 54.0 and x <= 59.0:
        return ('greitis', x, ', 1 taškas')
    elif x > 59.0 and x <= 64.0:
        return ('greitis', x, ', 2 taškai')
    elif x > 64.0 and x <= 69.0:
        return ('greitis', x, ', 3 taškai')
    elif x > 69.0 and x <= 74.0:
        return ('greitis', x, ', 4 taškai')
    elif x > 74.0 and x <= 79.0:
        return ('greitis', x, ', 5 taškai')
    elif x > 79.0 and x <= 84.0:
        return ('greitis', x, ', 6 taškai')
    elif x > 84.0 and x <= 89.0:
        return ('greitis', x, ', 7 taškai')
    elif x > 89.0:
        return ('greitis', x, ', 8 taškai, atimamos teisės')
    else:
        return ('Viršijote leistiną greitį, Jūsų greitis:', x, 'įspėjimas')

print(greitis())







