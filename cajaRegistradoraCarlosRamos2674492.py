#Carlos Andrés Ramos Velasquez - 18-08-2023
#Programación - 2674492

#Definición de función total más impuesto
def calcular_total(subtotal):
    impuesto = subtotal * 0.19
    total = subtotal + impuesto
    return total

#Mensaje bienvenida
print("Bienvenido a la caja registradora")

articulos = []
subtotal = 0

#Estructura de ingreso de productos
while True:
    nombre = input("Ingrese el nombre del artículo (o 'fin' para terminar): ")
    if nombre.lower() == 'fin':
        break

    cantidad = int(input("Ingrese la cantidad del artículo: "))
    valor = float(input("Ingrese el valor del artículo: "))

    total_articulo = cantidad * valor
    subtotal += total_articulo

    articulos.append((nombre, cantidad, valor, total_articulo))

#Impresión de factura
print("\nFactura:")
for articulo in articulos:
    print(f"{articulo[1]} {articulo[0]} a {articulo[2]} por unidad = {articulo[3]}")

print(f"\nSubtotal: {subtotal}")
total = calcular_total(subtotal)
print(f"Total con impuestos: {total}")