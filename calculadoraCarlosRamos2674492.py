#Carlos Andrés Ramos Velásquez - 18-07-2023
#Programación - Ficha:2674492

#Definición de funciones
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir entre cero"

#Menú de selección
while True:
    print("Opciones:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = int(input("Selecciona una opción: "))

    if opcion == 5:
        print("¡Hasta luego!")
        break

#Definición de variables
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

#Estructuras
    if opcion == 1:
        print("Resultado:", suma(num1, num2))
    elif opcion == 2:
        print("Resultado:", resta(num1, num2))
    elif opcion == 3:
        print("Resultado:", multiplicacion(num1, num2))
    elif opcion == 4:
        print("Resultado:", division(num1, num2))
    else:
        print("Opción inválida")
