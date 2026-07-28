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

def cambiar_estado():
    print("Clientes Disponibles:")
    
    for i, cliente in enumerate(clientes):
        print(i +1,"-", cliente["nombre"])
        
    seleccion =int(input("Seleccione el cliente: "))

    cliente = clientes[seleccion - 1]

    print("Estado actual:", cliente.get("estado", "pendiente"))

    print("1. Pendiente")
    print("2. En proceso")
    print("3. Finalizado")
    print("4. Entregado")

    estado = input("Seleccione el nuevo estado: ")

    estados= {
    "1": "pendiente",
    "2": "en proceso",
    "3": "finalizado",
    "4": "entregado"
}

    cliente["estado"] = estados.get(estado, "pendiente")

    guardar_clientes()

    print("Estado actualizado correctamente.")
    
def ver_resumen():
        total_clientes = len(clientes)
        pendientes = 0
        en_proceso = 0
        finalizados = 0
        entregados = 0
        ingresos = 0
        for cliente in clientes:
            if cliente.get("estado") == "pendiente":
                pendientes += 1
            elif cliente.get("estado") == "en proceso":
                en_proceso += 1
            elif cliente.get("estado") == "finalizado":
                finalizados += 1
            elif cliente.get("estado") == "entregado":
                entregados += 1
            ingresos += cliente.get("precio", 0)
            ingresos_formateados = f"{ingresos:,.0f}".replace(",", ".")
        print()
        print("===========================================")
        print("                 RESUMEN PRINTFLOW")
        print("===========================================")
        print("Total de clientes registrados:", total_clientes)
        print()
        print("Clientes pendientes:", pendientes)
        print("Clientes en proceso:", en_proceso)
        print("Clientes finalizados:", finalizados)
        print("Clientes entregados:", entregados)
        print()
        print("Ingresos totales: $" + ingresos_formateados)
        print("===========================================")
while True:
    print("==========================================")
    print("              PRINTFLOW")
    print("==========================================")
    print("Sistema de gestión de impresión")
    print()
    print("1. Registrar cliente")
    print("2. Mostrar clientes")
    print("3. Cambiar estado")
    print("4. Ver resumen")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del cliente: ")
        telefono = input("Ingrese el número de teléfono del cliente: ")
        trabajo = input("Ingrese el tipo de trabajo de solicitado: ")
        precio = float(input("Ingrese el precio del trabajo: "))
        estado = "pendiente"
        cliente = {
            "nombre": nombre,
            "telefono": telefono,
            "trabajo": trabajo,
            "precio": precio,  
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
            
            if cliente.get("precio",0) > 0:
                precio_formateado = f"{cliente['precio']:,.0f}".replace(",", ".")
                print("Precio: $" + precio_formateado)
            else:
                print("Precio: Sin Cargar")

            print("--------------------------")
    elif opcion == "3":
        cambiar_estado()
    elif opcion == "4":
        ver_resumen()
    elif opcion == "5":
        print("Cerrando el PrintFlow.")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")