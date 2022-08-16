# num_1 = int(input('Escoge un entero: '))
# num_2 = int(input('Escoge un segundo numero: '))

# if num_1 > num_2:
#     print('El primero numero es mayor que el segundo')
# elif num_1 < num_2:
#     print('El primer numero es menor que el segundo')
# else:
#     print('Los numeros son igual

name_user1 = input('Usuario 1 - Ingrese su nombre: ')
edad_user1 = int(input('Ingrese su edad: '))

name_user2 = input('Usuario 2 - Ingrese su nombre: ')
edad_user2 = int(input('Ingrese su edad: '))

if edad_user1 > edad_user2:
    print(f"{name_user1} es más grande que {name_user2}")
elif edad_user1 < edad_user2:
    print(f"{name_user1} es más chico que {name_user2}")
else:
    print(f"Ambos tienen la misma edad")