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
    
def pedir_telefono(mensaje):
    while True:
        telefono = input(mensaje)
        if telefono.strip() == "":
            print("El teléfono solo puede contener números.")
        elif not telefono.isdigit():
            print("Ingrese un número válido.")
        else:
            return telefono
def pedir_precio(mensaje):
    while True:
        precio = input(mensaje)
        if precio.strip() == "":
            print("El precio no puede estar vacío.")
            continue
        else:
           
            try:
                precio = float(precio)
                
                if precio < 0:
                    print("El precio no puede ser negativo.")
                    continue
                return precio
            
            except ValueError:
                print("Precio inválido. Por favor, ingrese un número válido.") 
                      
def validar_precio(precio):
    if precio.strip() == "":
        return False

    try:
        precio = float(precio)

        if precio < 0:
            return False

        return True

    except ValueError:
        return False
    
def pedir_texto(mensaje):
    while True:
        texto = input(mensaje)

        if texto.strip() == "":
            print("El valor no puede estar vacío.")
        else:
            break

    return texto

def cambiar_estado():
    print("Clientes Disponibles:")
    
    for i, cliente in enumerate(clientes):
        print(i + 1, "-", cliente["nombre"])
    
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
def validar_telefono(telefono):
    if telefono.strip() =="":
        return False   
    if not telefono.isdigit():
        return False
    if len(telefono) < 7 or len(telefono) > 15:
        return False
    
    return True

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
    if cliente.get("precio", 0) > 0:
                print("Precio: $", cliente["precio"])
    else:
        print("Precio: Sin Cargar")
     
    print("Estado:", cliente.get("estado", "pendiente"))
    
    nuevo_nombre= input("Ingrese el nuevo nombre: ")
    if nuevo_nombre:
        cliente["nombre"] = nuevo_nombre
        
    while True:
        nuevo_telefono = input("Ingrese el nuevo teléfono: ")

        if nuevo_telefono == "":
            break

        elif validar_telefono(nuevo_telefono):
            cliente["telefono"] = nuevo_telefono
            break

        else:
            print("Teléfono inválido. Ingrese un número válido.")


    nuevo_trabajo = input("Ingrese el nuevo trabajo: ")

    if nuevo_trabajo:
        cliente["trabajo"] = nuevo_trabajo


    while True:
        nuevo_precio = input("Ingrese el nuevo precio: ")

        if nuevo_precio == "":
            break

        elif validar_precio(nuevo_precio):
            cliente["precio"] = float(nuevo_precio)
            break

        else:
            print("Precio inválido. Ingrese un número válido.")


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
        nombre = pedir_texto("Ingrese el nombre del cliente: ")
        telefono = pedir_telefono("Ingrese el número de teléfono del cliente: ")
        trabajo = pedir_texto("Ingrese el tipo de trabajo solicitado: ")
        precio = pedir_precio("Ingrese el precio del trabajo: ")
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
        
        
        
        
    