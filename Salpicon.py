# Definir una lista para almacenar las frutas
frutas = []

# Solicitar al usuario la cantidad de frutas
n = int(input("Ingrese la cantidad de frutas: "))

# Pedir información de cada fruta y agregarla a la lista
for i in range(n):
    print(f"Ingrese los datos de la fruta {i + 1}:")
    id_fruta = int(input("ID de la fruta: "))
    nombre_fruta = input("Nombre de la fruta: ")
    precio_unitario = float(input("Precio unitario de la fruta: "))
    cantidad = int(input("Cantidad de la fruta: "))
    
    # Calcular el costo total de la fruta
    costo_total = precio_unitario * cantidad
    
    # Agregar la fruta a la lista
    fruta = {
        "ID": id_fruta,
        "Nombre": nombre_fruta,
        "Precio Unitario": precio_unitario,
        "Cantidad": cantidad,
        "Costo Total": costo_total
    }
    frutas.append(fruta)

# Función para obtener el costo total de un salpicón
def costo_salpicon():
    total_salpicon = sum(fruta["Costo Total"] for fruta in frutas)
    return total_salpicon

# Función para mostrar las frutas ordenadas por costo total (de mayor a menor)
def mostrar_frutas_ordenadas():
    frutas_ordenadas = sorted(frutas, key=lambda x: x["Costo Total"], reverse=True)
    for fruta in frutas_ordenadas:
        print(f"ID: {fruta['ID']}, Nombre: {fruta['Nombre']}, Costo Total: {fruta['Costo Total']}")

# Función para mostrar la fruta más barata y la más cara
def fruta_mas_barata_y_cara():
    frutas_ordenadas = sorted(frutas, key=lambda x: x["Precio Unitario"])
    fruta_mas_barata = frutas_ordenadas[0]
    fruta_mas_cara = frutas_ordenadas[-1]
    return fruta_mas_barata, fruta_mas_cara

# Mostrar opciones al usuario
while True:
    print("\nOpciones:")
    print("1. Calcular el costo total de un salpicón")
    print("2. Mostrar todas las frutas ordenadas por costo total (de mayor a menor)")
    print("3. Mostrar la fruta más barata y la más cara")
    print("4. Salir")
    
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        costo_total_salpicon = costo_salpicon()
        print(f"El costo total de un salpicón es: {costo_total_salpicon}")
    elif opcion == 2:
        mostrar_frutas_ordenadas()
    elif opcion == 3:
        fruta_barata, fruta_cara = fruta_mas_barata_y_cara()
        print(f"Fruta más barata: {fruta_barata['Nombre']}, Precio Unitario: {fruta_barata['Precio Unitario']}")
        print(f"Fruta más cara: {fruta_cara['Nombre']}, Precio Unitario: {fruta_cara['Precio Unitario']}")
    elif opcion == 4:
        break
    else:
        print("Opción no válida. Intente de nuevo.")
