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
    
    try:
        seleccion = int(input("Seleccione el cliente: "))
        if seleccion < 1 or seleccion > len(clientes):
            print("Selección inválida.")
            return
    
    except ValueError:
        print("Ingrese un número válido.")
        return
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
    if estado in estados:
        cliente["estado"] = estados[estado]
        guardar_clientes()
        print("Estado actualizado correctamente.")
    else:
        print("Selección inválida. Seleccione una opción válida entre 1 y 4.")
    
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
 
def buscar_cliente():
        nombre_buscar = input("Ingrese el nombre del cliente: ")
    
        encontrado = False
    
        for cliente in clientes:
           if cliente["nombre"].lower() == nombre_buscar.lower():
            print()
            print("===========================================")
            print("Nombre:", cliente["nombre"])
            print("Teléfono:", cliente["telefono"])
            print("Trabajo:", cliente["trabajo"])
            print("Estado:", cliente.get("estado", "pendiente"))
            
            if cliente.get("precio",0) > 0:
                precio_formateado = f"{cliente['precio']:,.0f}".replace(",", ".")
                print("Precio: $" + precio_formateado)
            else:
                print("Precio: Sin Cargar")
            print("===========================================")
            
            encontrado = True
            break
        if not encontrado:
         print("Cliente no encontrado.")
def editar_cliente():
    print("Clientes Disponibles:")
    
    for i, cliente in enumerate(clientes): 
    
        print(i + 1, "-", cliente["nombre"])
             
    try:
        seleccion = int(input("Seleccione el cliente: "))
        if seleccion < 1 or seleccion > len(clientes):
            print("Selección inválida.")
            return
    
    except ValueError:
        print("Ingrese un número válido.")
        return
    cliente = clientes[seleccion - 1]

    print()
    print("Cliente Seleccionado:")
    print("Nombre:", cliente["nombre"])
    print("Teléfono:", cliente["telefono"])
    print("Trabajo:", cliente["trabajo"])
    print("Precio:", cliente.get("precio", 0))
    print("Estado:", cliente.get("estado", "pendiente"))
    
    nuevo_nombre= input("Ingrese el nuevo nombre (ENTER para mantener): ")
    if nuevo_nombre:
        cliente["nombre"] = nuevo_nombre
        
    nuevo_telefono = input("Ingrese el nuevo teléfono (ENTER para mantener): ")
    if nuevo_telefono:
        cliente["telefono"] = nuevo_telefono
        
    nuevo_trabajo = input("Ingrese el nuevo trabajo (ENTER para mantener): ")
    if nuevo_trabajo:
        cliente["trabajo"] = nuevo_trabajo
        
    nuevo_precio = input("Ingrese el nuevo precio (ENTER para mantener): ")
    if nuevo_precio:
        try:
            cliente["precio"] = float(nuevo_precio)
    
            cliente["precio"] = float(nuevo_precio)
        except ValueError:
            print("Precio inválido. Se mantendrá el valor anterior.")
        
    guardar_clientes()
    print("Cliente actualizado correctamente.")
        
def eliminar_cliente():
    print("Clientes Disponibles:")
       
    for i, cliente in enumerate(clientes):
        print(i + 1, "-", cliente["nombre"])
        
    try:    
        seleccion = int(input("Seleccione el cliente a eliminar: "))
    
        if seleccion < 1 or seleccion > len(clientes):
            print("Selección inválida.")
            return
    
    except ValueError:
        print("Ingrese un número válido.")
        return

    cliente = clientes[seleccion - 1]
        
    print()
    print("Cliente Seleccionado:") 
    print("Nombre:", cliente["nombre"])
    print("Trabajo:", cliente["trabajo"])
        
    confirmacion = input("¿Está seguro de eliminar este cliente? (s/n): ")
       
    if confirmacion.lower() == "s":
            del clientes[seleccion - 1]
            guardar_clientes()
            print("Cliente eliminado correctamente.")
    else:
            print("Operación cancelada.")
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
    print("5. Buscar cliente")
    print("6. Editar Cliente")
    print("7. Eliminar cliente")
    print("8. Salir")
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
        buscar_cliente()
    elif opcion == "6":
        editar_cliente()
    elif opcion == "7":
        eliminar_cliente()
    elif opcion == "8":  
        print("Cerrando el PrintFlow.")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")