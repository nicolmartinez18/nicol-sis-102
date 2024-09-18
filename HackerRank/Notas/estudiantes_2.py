estudiantes = {
 "Jose Sandoval": [90, 80, 70],
    "Eduardo Llanos": [95, 85, 75],
    "Camila Rios": [98, 92, 88]
}

def calcular_promedio(calificaciones):

#Calcula el promedio de una lista de calificaciones

    return sum(calificaciones) / len(calificaciones)

promedios = {}
for estudiante, calificaciones in estudiantes.items():
    promedios[estudiante] = calcular_promedio(calificaciones)

while True:
    print("Opciones:")
    print("1. Imprimir promedios")
    print("2. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        for estudiante, promedio in promedios.items():
            print(f"El promedio de {estudiante} es {promedio:.2f}")
    elif opcion == "2":
        print("Saliendo...")
        break
    else:
        print("Opción inválida. Intente nuevamente.")