p = float(input("tu peso en Kgs "))
a = float(input('tu altura en metros '))

imc = (p / (a**2))
imc = round(imc, 2)
print('Tu índice de masa corporal es:', imc)
