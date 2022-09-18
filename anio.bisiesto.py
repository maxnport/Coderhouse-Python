def verificar_anio(anio):
    if anio % 100 != 0 and anio % 400 == 0 or anio % 4 ==0:
        print('Es bisiesto')
    else:
        print('No es bisiesto')

verificar_anio(2012)
verificar_anio(2010)
verificar_anio(2000)
verificar_anio(1900)