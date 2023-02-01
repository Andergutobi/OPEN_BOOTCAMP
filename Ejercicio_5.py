def bisiesto(year):
    if year %4 == 0 and year % 100 != 0:
        if year % 400 == 0:
            print('el año', year,'es bisiesto.')
    elif year % 4 != 0:
        print('el año', year, 'no es bisiesto')
year = int(input('Introduce el año que quieras saber si es bisiesto. '))
bisiesto(year)
