import funciones_conversion

def main():
    print("Calculadora de Conversiones")
    print("---------------------")

    while True:
        print("Elige una conversión:")
        print("1. Longitud (metros a kilómetros)")
        print("2. Masa (gramos a kilogramos)")
        print("3. Temperatura (Celsius a Fahrenheit)")
        print("4. Salir")

        eleccion = input("Ingresa tu elección: ")

        if eleccion == "1":
            metros = float(input("Ingresa metros: "))
            kilometros = conversions.metros_a_kilometros(metros)
            print(f"{metros} metros es igual a {kilometros} kilómetros")

        elif eleccion == "2":
            gramos = float(input("Ingresa gramos: "))
            kilogramos = conversions.gramos_a_kilogramos(gramos)
            print(f"{gramos} gramos es igual a {kilogramos} kilogramos")

        elif eleccion == "3":
            celsius = float(input("Ingresa Celsius: "))
            fahrenheit = conversions.celsius_a_fahrenheit(celsius)
            print(f"{celsius} Celsius es igual a {fahrenheit} Fahrenheit")

        elif eleccion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Elección inválida. Por favor, inténtalo de nuevo.")

if __name__ == "__main__":
    main()