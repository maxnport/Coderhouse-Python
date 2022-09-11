#Ejercicio 1
# un_num = float(input('Ingrese un número: '))
# otro_num = float(input('Ingrese otro número: '))

# opciones = input('Elija una opcion:\n 1- Suma\n 2-Resta\n 3-Multiplicación\n 4-Salir\n')

# if opciones == '1':
#     suma = un_num + otro_num
#     print(f'El resultado de la suma es: {suma}')

# elif opciones == '2':
#     resta = un_num - otro_num
#     print(f'El resultado de la resta es {resta}')

# elif opciones == '3':
#     multi = un_num * otro_num
#     print(f'El resultado de la multiplicación es {multi}')

# elif opciones == '4':
#     pass

# else:
#     print('Opción invalida')

#Ejercicio 2

# num = 2

# while num % 2 != 1:
#     num = float(input('Ingrese un número: '))
# else:
#     print("El número ingresado es impar")

#Ejercicio 3
# suma = 0
# valor = 0
# while valor != 100:
#     for valor in range(101):
#         if valor % 2 == 0:
#             continue
#         else:
#             suma += valor
# print(suma)
    

#Ejercicio 4

# cantidad_num = int(input('Que cantidad de números va a ingresar?: '))
# acumulador = 0
# suma = 0

# while acumulador < cantidad_num:
#     numeros = float(input('Ingrese un número: '))
#     acumulador += 1
#     suma = suma + numeros
# else:
#     promedio = suma / cantidad_num
#     print(f'El promedio es {promedio}')

#Ejercicio 5

# numeros = [1, 3, 6, 9]
# numero_ingresado = 11

# while numero_ingresado < 0 or numero_ingresado > 9:
#     numero_ingresado = int(input('Ingrese un numero del 0 al 9: '))
# else:
#     if numero_ingresado in numeros:
#         print('El número esta en la lista! :D')
#     else:
#         print('Lamentablemente el número no se encuentra en la lista :(')

#Ejercicio 6

# cero_diez = list(range(0,11))
# print(cero_diez)

# menosdiez_cero = list(range(-10,1))
# print(menosdiez_cero)

# pares = list(range(0,21,2))
# print(pares)

# impares = list(range(-19,0,2))
# print(impares)

# multiplo_cinco = list(range(0,51,5))
# print(multiplo_cinco)

#Ejercicio 7

lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
lista_3 = []

for i in lista_1:
    if i in lista_2:
        lista_3.append(i)
    else:
        continue

print(lista_3)
