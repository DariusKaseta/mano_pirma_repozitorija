
def greitis():
    
    x = int(input('Iveskite greiti:'))
    
    if x <= 50:
        return(x, 'ok')
    elif x > 54 and x <= 59:
        return ('greitis', x, ', 1 taskas')
    elif x > 59 and x <= 64:
        return ('greitis', x, ', 2 taskai')
    elif x > 64 and x <= 69:
        return ('greitis', x, ', 3 taskai')
    elif x > 69 and x <= 74:
        return ('greitis', x, ', 4 taskai')
    elif x > 74 and x <= 79:
        return ('greitis', x, ', 5 taskai')
    elif x > 79 and x <= 84:
        return ('greitis', x, ', 6 taskai')
    elif x > 84 and x <= 89:
        return ('greitis', x, ', 7 taskai')
    elif x > 89 and x <= 90:
        return ('greitis', x, ', 8 taskai, atimamos teises')
    else:
        return ('virsijote greiti, Jusu greitis:', x, 'ispejimas')

print(greitis())







