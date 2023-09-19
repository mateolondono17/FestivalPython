# Lista para almacenar las agrupaciones musicales
agrupaciones = []

def registrar_agrupacion():
    id = input("Ingrese el ID de la agrupación: ")
    nombre = input("Ingrese el nombre de la agrupación: ")
    genero = input("Ingrese el género de la agrupación: ")
    hora_presentacion = input("Ingrese la hora de presentación (HH:MM): ")
    pago = float(input("Ingrese el pago para la agrupación: "))
    estado = False  # Inicialmente, la agrupación no se ha presentado
    
    agrupacion = {
        'id': id,
        'nombre': nombre,
        'genero': genero,
        'hora_presentacion': hora_presentacion,
        'pago': pago,
        'estado': estado
    }
    
    agrupaciones.append(agrupacion)
    print(f"Agrupación {nombre} registrada con éxito!")

def mostrar_agrupaciones_no_presentadas():
    print("Agrupaciones que no se han presentado:")
    for agrupacion in agrupaciones:
        if not agrupacion['estado']:
            print(f"ID: {agrupacion['id']}, Nombre: {agrupacion['nombre']}, Hora de Presentación: {agrupacion['hora_presentacion']}")

def cambiar_hora_presentacion():
    id_buscar = input("Ingrese el ID de la agrupación cuya hora de presentación desea cambiar: ")
    nueva_hora = input("Ingrese la nueva hora de presentación (HH:MM): ")
    
    for agrupacion in agrupaciones:
        if agrupacion['id'] == id_buscar and not agrupacion['estado']:
            agrupacion['hora_presentacion'] = nueva_hora
            print(f"Hora de presentación de {agrupacion['nombre']} cambiada a {nueva_hora}")
            return
    
    print("La agrupación no se encuentra en la lista o ya se ha presentado.")

def retirar_agrupacion():
    id_buscar = input("Ingrese el ID de la agrupación que desea retirar: ")
    
    for agrupacion in agrupaciones:
        if agrupacion['id'] == id_buscar and not agrupacion['estado']:
            agrupaciones.remove(agrupacion)
            print(f"Agrupación {agrupacion['nombre']} retirada de la lista.")
            return
    
    print("La agrupación no se encuentra en la lista o ya se ha presentado.")

while True:
    print("\nMenú de Opciones:")
    print("1. Registrar una agrupación")
    print("2. Mostrar agrupaciones no presentadas")
    print("3. Cambiar hora de presentación")
    print("4. Retirar una agrupación")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        registrar_agrupacion()
    elif opcion == '2':
        mostrar_agrupaciones_no_presentadas()
    elif opcion == '3':
        cambiar_hora_presentacion()
    elif opcion == '4':
        retirar_agrupacion()
    elif opcion == '5':
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
