#calculadora
#suma
def suma(x,y):
    return x + y
#resta
def resta(x,y):
    return x - y
#multiplicacion
def multiplicacion (x,y):
    return x * y
#division
def division(x,y):
    if y==0:
        rise ("no se puede dividir por 0")
    return x / y
print("1.suma")
print("2.resta")
print("3.multiplicacion")
print("4.division")
opcion= input("ingrese opcion:")
if opcion=="1":
    num1=float(input("ingrese el primer numero:"))
    num2=float(input("ingrese el segundo numero:"))
    print (f "la suma es:{suma(num1,num2)}")
elif opcion=="2":
