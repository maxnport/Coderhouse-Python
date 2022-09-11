def verificar_anio(anio):
    if anio % 100 != 0 and anio % 4 ==0 or anio % 400 == 0:
        print('Es bisiesto')
    else:
        print('No es bisiesto')

verificar_anio(1700)
verificar_anio(1800)
verificar_anio(1600)
verificar_anio(2400)