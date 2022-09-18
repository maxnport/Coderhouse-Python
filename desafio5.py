#Ejercicio 1

def area_rectangulo(base, altura):
    resultado_rectangulo = base * altura
    print(f'El area del rectangulo es {resultado_rectangulo}')

area_rectangulo(15,10)

#Ejercicio 2
from ast import parse
import math
def area_circulo(radio):
    resultado_ciruclo = (radio**2)*math.pi
    print(f'El area del circulo es {resultado_ciruclo}')

area_circulo(2)

#Ejercicio 3

def relacion(valor1, valor2):
    if valor1 > valor2:
        return 1
    elif valor1 < valor2:
        return -1
    else:
        relacion = 0
        return  0

assert(relacion(5, 10) == -1)
assert(relacion(10, 5) == 1)
assert(relacion(5, 5) == 0)

#Ejercicio 4

def intermedio(num1, num2):
    return (num1 + num2) / 2

assert(intermedio(-12, 24) == 6)

#Ejercicio 5

def recortar(a_recortar, inferior, superior):
    if a_recortar < inferior:
        return inferior
    elif a_recortar > superior:
        return superior
    else:
        return a_recortar

assert(recortar(15, 0, 10) == 10)

#Ejercicio 6

def separar(lista):
    pares = []
    impares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
            pares.sort()
        else:
            impares.append(i)
            impares.sort()
    print(f'Pares: {pares} Impares: {impares}')

separar([1,2,3,4,5,6,7,8,9])

        