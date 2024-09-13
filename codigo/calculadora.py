# suma
def suma(x, y):
    return x + y

# resta
def resta(x, y):
    return x - y

# multiplicacion
def multiplicacion(x, y):
    return x * y

# division
def division(x, y):
    if y == 0:
        raise ValueError("No se puede dividir por 0")
    return x / y

print("1. suma")
print("2. resta")
print("3. multiplicacion")
print("4. division")

opcion = input("Ingrese opción: ")

if opcion == "1":
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print(f"La suma es: {suma(num1, num2)}")
elif opcion == "2":
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print(f"La resta es: {resta(num1, num2)}")
elif opcion == "3":
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print(f"La multiplicación es: {multiplicacion(num1, num2)}")
elif opcion == "4":
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    try:
        print(f"La división es: {division(num1, num2)}")
    except ValueError as e:
        print(f"Error: {e}")