from decimal import Decimal, ROUND_HALF_UP

class PaskolosSkaiciuokle:
    def menesine_imoka(self, paskolos_dydis, metines_palukanos, terminas):
        menesines_palukanos = metines_palukanos / 12
        laikotarpis = terminas * 12
        koeficiantas = ((1 + menesines_palukanos) ** laikotarpis * menesines_palukanos) / (((1 + menesines_palukanos) ** laikotarpis) - 1)
        menesinis_mokejimas = paskolos_dydis * koeficiantas
        return (menesinis_mokejimas)
    
    def bendra_suma(self, paskolos_dydis, metines_palukanos, terminas):
        imoka = self.menesine_imoka(paskolos_dydis, metines_palukanos, terminas)
        suma = imoka * terminas *12
        suma = Decimal(str(imoka)) * Decimal(str(terminas)) * Decimal('12') * Decimal(str(paskolos_dydis))
        suapvalinta = suma.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        return (suapvalinta)