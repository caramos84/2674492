#Carlos Andrés Ramos Velasquez - 01-09-2023
#Programación - 2674492

import datetime

# Paso 1: Solicitar nombre de Usuario (empleado)
nombre_empleado = input("Ingrese su nombre de usuario (empleado): ")

# Paso 2: Solicitar fecha de nacimiento (DD/MM/AAAA)
fecha_nacimiento_str = input("Ingrese su fecha de nacimiento (DD/MM/AAAA): ")
fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y")
hoy = datetime.datetime.now()
edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

if edad >= 18:
    # Paso 3: Si es mayor de edad, solicitar información del cliente
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    id_cliente = input("Ingrese el ID del cliente: ")
    direccion_cliente = input("Ingrese la dirección del cliente: ")
    telefono_cliente = input("Ingrese el teléfono del cliente: ")

# Inicializar variables para la factura
productos = []
subtotal = 0

while True:
    # Paso 4: Ingresar nombre del producto
    nombre_producto = input("Ingrese el nombre del producto: ")
    
    # Paso 5: Ingresar código de producto
    codigo_producto = input("Ingrese el código del producto: ")
    
    # Paso 6: Ingresar valor unitario
    valor_unitario = float(input("Ingrese el valor unitario del producto: "))
    
    # Paso 7: Ingresar cantidad de productos
    cantidad = int(input("Ingrese la cantidad de productos: "))
    
    # Calcular el subtotal para este producto
    total_producto = valor_unitario * cantidad
    subtotal += total_producto
    
    # Agregar el producto a la lista
    productos.append({
        "nombre": nombre_producto,
        "codigo": codigo_producto,
        "valor_unitario": valor_unitario,
        "cantidad": cantidad,
        "total": total_producto
    })
    
    # Paso 8: Preguntar si ingresar otro producto
    otro_producto = input("¿Desea ingresar otro producto? (si/no): ")
    if otro_producto.lower() != "si":
        break

# Paso 9: Calcular subtotal
iva = subtotal * 0.19  # Paso 10: Calcular IVA (19%)
total_factura = subtotal + iva  # Paso 11: Calcular total factura

# Paso 12: Imprimir factura
print("\n*** Factura ***")
print(f"Empleado: {nombre_empleado}")
if edad >= 18:
    print(f"Cliente: {nombre_cliente}")
    print(f"ID Cliente: {id_cliente}")
    print(f"Dirección Cliente: {direccion_cliente}")
    print(f"Teléfono Cliente: {telefono_cliente}")

print("\nProductos:")
for producto in productos:
    print(f"Nombre: {producto['nombre']}, Código: {producto['codigo']}, Valor Unitario: ${producto['valor_unitario']:.2f}, Cantidad: {producto['cantidad']}, Total: ${producto['total']:.2f}")

print(f"\nSubtotal: ${subtotal:.2f}")
print(f"IVA (19%): ${iva:.2f}")
print(f"Total Factura: ${total_factura:.2f}")
