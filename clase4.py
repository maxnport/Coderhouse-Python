anio_nacimiento = int(input("Ingrese año de nacimiento: "))

if anio_nacimiento >= 1920 and anio_nacimiento <= 1940:
    print("silenciosa")

elif anio_nacimiento >= 1940 and anio_nacimiento <= 1964:
    print("baby boomer")

elif anio_nacimiento >= 1965 and anio_nacimiento <= 1979:
    print("baby boomer")

elif anio_nacimiento >= 1980 and anio_nacimiento <= 2000:
    print("baby boomer")

elif anio_nacimiento >= 2001 and anio_nacimiento <= 2010:
    print("baby boomer")

else:
    print("No hay generacion en este año")