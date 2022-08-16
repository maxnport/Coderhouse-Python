nota_1 = int(input("Ingrese la primer nota: "))
nota_2 = int(input("Ingrese la segunda nota: "))
nota_3 = int(input("Ingrese la tercer nota: "))

calculo_promedio = str((nota_1 * 0.1 + nota_2 * 0.3 + nota_3 * 0.5) / (0.2 + 0.3 + 0.5))

mostrar_promedio = print("El promedio ponderado de las notas es: " + calculo_promedio)
