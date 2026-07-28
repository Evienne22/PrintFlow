import json
def cargar_clientes():
    try:
        with open("clientes.json", "r") as archivo:
            return json.load(archivo)
    except:
        return []
clientes = cargar_clientes()
def guardar_clientes():
    with open("clientes.json", "w") as archivo:
        json.dump(clientes, archivo, indent=4)
while True:
    print("==========================================")
    print("              PRINTFLOW")
    print("==========================================")
    print("Sistema de gestión de impresión")
    print()
    print("1. Registrar cliente")
    print("2. Mostrar clientes")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del cliente: ")
        telefono = input("Ingrese el número de teléfono del cliente: ")
        trabajo = input("Ingrese el tipo de trabajo de solicitado: ")
        estado = "pendiente"
        cliente = {
            "nombre": nombre,
            "telefono": telefono,
            "trabajo": trabajo,
            "estado": estado
        }
        clientes.append(cliente)
        guardar_clientes()
        print()
        print("Cliente registrado correctamente.")
        
    elif opcion == "2":
        print()
        print("Lista de clientes:")
        for cliente in clientes:
            print("--------------------------")
            print("Nombre: " + cliente["nombre"])
            print("Teléfono: " + cliente["telefono"])
            print("Trabajo: " + cliente["trabajo"])
            print("Estado: " + cliente.get("estado", "pendiente"))
    elif opcion == "3":
        print("Cerrando el PrintFlow.")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")