nombres = []
notas = []  

while True:
    print("1. Agregar nombre")
    print("2. Agregar nota")
    print("3. Mostrar nombres")
    print("4. Buscar nombre")
    print("5. Salir")
    opcion = int(input("Ingrese su opción: "))
    
    if opcion == 1:
        nombres.append(input("Ingrese un nombre: "))
        print("Nombre agregado con éxito!")
    elif opcion == 2:
        notas.append(input("Ingrese notas: "))  
        print("Nota agregada con éxito!")
    elif opcion == 3:
        for i, nombre in enumerate(nombres):
            print(f"{i+1}. {nombre}")
    elif opcion == 4:
        nombre = input("Ingrese el nombre a buscar: ")
        if nombre in nombres:
            print("Nombre encontrado")
        else:
            print("Nombre no encontrado")
    elif opcion == 5:
        break
    else:
        print("Opción inválida")