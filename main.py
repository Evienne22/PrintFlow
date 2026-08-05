import json
from datetime import datetime
def cargar_clientes():
    try:
        with open("clientes.json", "r") as archivo:
            return json.load(archivo)
    except:
        return []

def cargar_clientes_archivados():
    try:
        with open("clientes_archivados.json", "r") as archivo:
            return json.load(archivo)
    except:
        return []

def guardar_clientes_archivados():
    with open("clientes_archivados.json", "w") as archivo:
        json.dump(clientes_archivados, archivo, indent=4)
        
def guardar_clientes():
    with open("clientes.json", "w") as archivo:
        json.dump(clientes, archivo, indent=4)

clientes = cargar_clientes()

clientes_archivados = cargar_clientes_archivados()

def mostrar_cliente(cliente):
    print("ID:", cliente["id"])
    print("Nombre:", cliente["nombre"])
    print("Teléfono:", cliente["telefono"])
    print("Trabajo:", cliente["trabajo"])
    if cliente.get("precio", 0) > 0:
        precio_formateado = f"{cliente['precio']:,.0f}".replace(",", ".")
        print("Precio: $" + precio_formateado)
    else:
        print("Precio: Sin Cargar")
    print("Estado:", cliente.get("estado", "pendiente"))
    print("Fecha de creación:", cliente.get("fecha_creacion", "No registrado"))
    print("Fecha de entrega:", cliente.get("fecha_entrega", "No entregado"))
    
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
    
def validar_telefono(telefono):
    if telefono.strip() =="":
        return False   
    if not telefono.isdigit():
        return False
    if len(telefono) < 7 or len(telefono) > 15:
        return False
    
    return True

def generar_id():
    if clientes:
        ids = []

        for cliente in clientes:
            if "id" in cliente:
                ids.append(cliente["id"])

        if ids:
            return max(ids) + 1

    return 1


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
    
    for cliente in clientes:
        print(cliente["id"], "-", cliente["nombre"])
        
    id_buscado = int(input("Ingrese el ID del cliente: "))
    
    cliente_encontrado = None
    
    for cliente in clientes:
        if cliente ["id"] == id_buscado:
            cliente_encontrado = cliente
            break
    
    if cliente_encontrado is None:
        print("Cliente no encontrado.")
        return
    
    print("Estado actual del cliente:", cliente_encontrado.get("estado", "pendiente"))
    print("Opciones de estado:")    
    print("1. Pendiente")
    print("2. En proceso")
    print("3. Finalizado")
    print("4. Entregado")
    opcion_estados = input("Seleccione el nuevo estado: ")
    estado ={
        
        "1": "pendiente",
        "2": "en proceso",
        "3": "finalizado",
        "4": "entregado"
    }
    if opcion_estados in estado:
        cliente_encontrado["estado"] = estado[opcion_estados]
    
        if cliente_encontrado["estado"] == "entregado":
            cliente_encontrado["fecha_entrega"] = datetime.now().strftime("%d/%m/%Y")
    
        guardar_clientes()
        print("Estado actualizado correctamente.")
        
    else:
        print("Selección inválida.")
def ver_resumen():
        total_clientes = len(clientes)
        total_archivados = len(clientes_archivados)
        total_historicos = total_clientes + total_archivados
        
        pendientes = 0
        en_proceso = 0
        finalizados = 0
        entregados = 0
        
        ingresos = 0
        ingresos_historicos = 0
        
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
            
        for cliente in clientes_archivados:
            ingresos_historicos += cliente.get("precio", 0)

        ingresos_formateados = f"{ingresos:,.0f}".replace(",", ".")
        historicos_formateados = f"{ingresos_historicos:,.0f}".replace(",", ".") 
        total_formateados = f"{ingresos + ingresos_historicos:,.0f}".replace(",", ".")
        print()
        print("===========================================")
        print("                 RESUMEN PRINTFLOW")
        print("===========================================")
        print("Clientes Activos:", total_clientes)
        print("Clientes Archivados:", total_archivados)
        print("Total Histórico:", total_historicos)
        
        print()
        print("Clientes pendientes:", pendientes)
        print("Clientes en proceso:", en_proceso)
        print("Clientes finalizados:", finalizados)
        print("Clientes entregados:", entregados)
        
        print()
        print("Ingresos activos: $" + ingresos_formateados)
        print("Ingresos históricos: $" + historicos_formateados)
        print("Ingresos totales: $" + total_formateados)
        print("===========================================")
 
def buscar_cliente():
        nombre_buscar = input("Ingrese el nombre del cliente: ")
    
        encontrado = False
    
        for cliente in clientes:
           if cliente["nombre"].lower() == nombre_buscar.lower():
            print()
            print("===========================================")
            mostrar_cliente(cliente)
            print("===========================================")
            
            encontrado = True
            break
        if not encontrado:
         print("Cliente no encontrado.")

def editar_cliente():
    print("Clientes Disponibles:")
    
    for cliente in clientes:
        print(cliente["id"], "-", cliente["nombre"])
        
    try:
        id_buscado = int(input("Ingrese el ID del cliente: "))
        
    except ValueError:
        print("Ingrese un número válido.")
        return
    cliente_encontrado = None
    
    for cliente in clientes:
        if cliente["id"] == id_buscado:
            cliente_encontrado = cliente
            break
        
    if cliente_encontrado is None:
        print("Cliente no encontrado.")
        return

    print()
    mostrar_cliente(cliente_encontrado)

    print("Estado:", cliente_encontrado.get("estado", "pendiente"))
    
    nuevo_nombre= input("Ingrese el nuevo nombre: ")
    if nuevo_nombre:
        cliente_encontrado["nombre"] = nuevo_nombre
        
    while True:
        nuevo_telefono = input("Ingrese el nuevo teléfono: ")

        if nuevo_telefono == "":
            break

        elif validar_telefono(nuevo_telefono):
            cliente_encontrado["telefono"] = nuevo_telefono
            break

        else:
            print("Teléfono inválido. Ingrese un número válido.")


    nuevo_trabajo = input("Ingrese el nuevo trabajo: ")

    if nuevo_trabajo:
        cliente_encontrado["trabajo"] = nuevo_trabajo


    while True:
        nuevo_precio = input("Ingrese el nuevo precio: ")

        if nuevo_precio == "":
            break

        elif validar_precio(nuevo_precio):
            cliente_encontrado["precio"] = float(nuevo_precio)
            break

        else:
            print("Precio inválido. Ingrese un número válido.")


    guardar_clientes()
    print("Cliente actualizado correctamente.")
    
def mostrar_entregados():
    print("Clientes Entregados:")
    encontrado = False
    for cliente in clientes:
        if cliente.get("estado") == "entregado":
            encontrado = True
            print("--------------------------")
            mostrar_cliente(cliente)
    if not encontrado:
        print("No hay clientes entregados.")

def archivar_clientes_entregados():
    print("Clientes Entregados:")
       
    clientes_entregados = []
    
    for cliente in clientes:
            if cliente.get("estado") == "entregado":
                clientes_entregados.append(cliente)
                
    if not clientes_entregados:
            print("No hay clientes entregados para archivar.")
            return
    
    for i, cliente in enumerate(clientes_entregados):
                    print(i + 1, "-", cliente["nombre"])
    
    try:    
        seleccion = int(input("Seleccione el cliente a archivar: "))
    
        if seleccion < 1 or seleccion > len(clientes_entregados):
            print("Selección inválida.")
            return
    
    except ValueError:
        print("Ingrese un número válido.")
        return

    cliente = clientes_entregados[seleccion - 1]
        
    print()
    print("Cliente Seleccionado:") 
    mostrar_cliente(cliente)
        
    confirmacion = input("¿Está seguro de archivar este cliente? (s/n): ")
       
    if confirmacion.lower() == "s":
            clientes_archivados.append(cliente)
            guardar_clientes_archivados()
        
            clientes.remove(cliente)
            guardar_clientes()
            
            print("Cliente archivado correctamente.")
    else:
            print("Operación cancelada.")
def ver_clientes_archivados():
    print("Clientes Archivados:")
    if not clientes_archivados:
        print("No hay clientes archivados.")
        return
    
    for cliente in clientes_archivados:
        print("--------------------------")
        mostrar_cliente(cliente)                 
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
    mostrar_cliente(cliente)
        
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
    print("8. Archivar clientes entregados")
    print("9. Ver clientes archivados")
    print("10. Salir")
    print("==========================================")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = pedir_texto("Ingrese el nombre del cliente: ")
        telefono = pedir_telefono("Ingrese el número de teléfono del cliente: ")
        trabajo = pedir_texto("Ingrese el tipo de trabajo solicitado: ")
        precio = pedir_precio("Ingrese el precio del trabajo: ")
        estado = "pendiente"
        
        cliente = {
            "id": generar_id(),
            "nombre": nombre,
            "telefono": telefono,
            "trabajo": trabajo,
            "precio": precio,  
            "estado": estado,
            "fecha_creacion": datetime.now().strftime("%d/%m/%Y")
        }
        clientes.append(cliente)
        
        guardar_clientes()
        
        print()
        
        print("Cliente registrado correctamente.")
        
    elif opcion == "2":
        print()
        
        print("Lista de clientes:")
        
        for cliente in clientes:
            mostrar_cliente(cliente)
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
        archivar_clientes_entregados()
    elif opcion == "9":
        ver_clientes_archivados()
    elif opcion == "10":
        print("Cerrando el PrintFlow.")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")