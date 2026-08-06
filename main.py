import json
from datetime import datetime
def cargar_clientes():
    try:
        with open("clientes.json", "r") as archivo:
            return json.load(archivo)
        
    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Error: el archivo clientes.json está dañado.")
        return[]
    
def cargar_clientes_archivados():
    try:
        with open("clientes_archivados.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
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
    print("Cantidad:", cliente.get ("cantidad","No registrada"))
    if cliente.get("precio", 0) > 0:
        precio_formateado = f"{cliente['precio']:,.0f}".replace(",", ".")
        print("Precio: $" + precio_formateado)
    else:
        print("Precio: Sin Cargar")
    print("Estado:", cliente.get("estado", "pendiente"))
    print("Fecha de creación:", cliente.get("fecha_creacion", "No registrado"))
    print("Fecha de entrega:", cliente.get("fecha_entrega", "No entregado"))
    print("Fecha estima entrega:",cliente.get("fecha_entrega_estimada","No registrada"))
    
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
def pedir_cantidad(mensaje):
    while True:
        cantidad = input(mensaje)
        
        if cantidad.strip() == "":
            print("La cantidad no puede estar vacía.")
            continue
        
        try:
            cantidad = int(cantidad)
            
            if cantidad <= 0:
                print("La cantidad debe ser mayor a cero.")
                continue
        
            return cantidad
    
        except ValueError:
            print("Ingrese un número válido.")
            
def pedir_fecha(mensaje):
    while True:
        fecha = input(mensaje)
        
        try:
            datetime.strptime(fecha, "%d/%m/%Y")
            return fecha
        
        except ValueError:
            print("Fecha inválida. Use el formato día/mes/año.")
                
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
                
        for cliente in clientes_archivados:
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
    
        print("===========================================")
        print("              RESUMEN PRINTFLOW")
        print("===========================================")
        
        total_clientes = len(clientes)
        total_archivados = len(clientes_archivados)
        total_historicos = total_clientes + total_archivados
            
        print("Total Histórico:", total_historicos)
        print("Total Activo:", total_clientes)
        print("Total Archivado:", total_archivados)
        print("Total Pendientes:", sum(1 for cliente in clientes if cliente.get("estado") == "pendiente"))
        print("Total En Proceso:", sum(1 for cliente in clientes if cliente.get("estado") == "en proceso"))
        print("Total Finalizados:", sum(1 for cliente in clientes if cliente.get("estado") == "finalizado"))
        print("Total Entregados:", sum(1 for cliente in clientes if cliente.get("estado") == "entregado"))  
        print("===========================================")
        print("Ingresos Activos: $", f"{sum(cliente.get('precio', 0) for cliente in clientes):,.0f}".replace(",", "."))
        print("Ingresos Archivados: $", f"{sum(cliente.get('precio', 0) for cliente in clientes_archivados):,.0f}".replace(",", "."))
        print("Ingresos Totales: $", f"{sum(cliente.get('precio', 0) for cliente in clientes) + sum(cliente.get('precio', 0) for cliente in clientes_archivados):,.0f}".replace(",", "."))
        print("===========================================")
        print("Resumen de trabajos realizados:")
        
        trabajos = {} 
        unidades = {}
        
        for cliente in clientes + clientes_archivados:
            trabajo = cliente.get("trabajo", "No registrado")
            
            if trabajo in trabajos:
                trabajos[trabajo] += 1
            else:
                trabajos[trabajo] = 1
                
            cantidad = cliente.get("cantidad", 0)
        
            if trabajo in unidades:
                unidades[trabajo] += cantidad
            else:
                unidades[trabajo] = cantidad
            
            
        print()
        print("Trabajos realizados:")
        for trabajo, cantidad in trabajos.items():
            print(f"{trabajo}: {cantidad}")
            
        print()
        print("Producción realizada: ")
        for trabajo, cantidad in unidades.items():
            print(f"{trabajo}: {cantidad} unidades")

def buscar_cliente():
    for cliente in clientes:
        print(cliente["id"], "-", cliente["nombre"])
    
    busqueda = input("Ingrese el ID o el nombre del cliente: ").lower()
    
    clientes_encontrados = None
    
    if busqueda.isdigit():
        id_buscado = int(busqueda)
        clientes_encontrados = [cliente for cliente in clientes if cliente["id"] == id_buscado]
    else:
        clientes_encontrados = [cliente for cliente in clientes if busqueda in cliente["nombre"].lower()]

    if clientes_encontrados:
        print("Clientes encontrados:")
        for cliente in clientes_encontrados:
            print("--------------------------")
            mostrar_cliente(cliente)
    else:
        print("No se encontró ningún cliente.")

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
    
    for cliente in clientes_entregados:
        print(cliente["id"], "-", cliente["nombre"])
        
    id_buscado = int(input("Ingrese el ID del cliente a archivar: "))
    
    cliente_encontrado = None
    
    for cliente in clientes_entregados:
        if cliente["id"] == id_buscado:
            cliente_encontrado = cliente
            break

    if cliente_encontrado is None:
        print("Cliente no encontrado.")
        return
    
    print()
    print("Cliente Seleccionado:")
    mostrar_cliente(cliente_encontrado)
    
    confirmacion = input("¿Está seguro de archivar este cliente? (s/n): ")
    
    if confirmacion.lower() == "s":
        clientes.remove(cliente_encontrado)
        clientes_archivados.append(cliente_encontrado)
        
        guardar_clientes()
       
        guardar_clientes_archivados()
        print("Cliente archivado correctamente.")

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
    for cliente in clientes:
            print(cliente["id"], "-", cliente["nombre"])
    try:
        id_buscado = int(input("Ingrese el ID del cliente a eliminar: ")) 
        
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
    print("Cliente Seleccionado:")
    mostrar_cliente(cliente_encontrado)
    
    confirmacion = input("¿Está seguro de eliminar este cliente? (s/n): ")
    
    if confirmacion.lower() == "s": 
        clientes.remove(cliente_encontrado)
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
        cantidad = pedir_cantidad("Ingrese la cantidad: ")
        fecha_entrega_estimada = pedir_fecha("Fecha estimadade entrega: ")
        estado = "pendiente"
        cliente = {
            "id": generar_id(),
            "nombre": nombre,
            "telefono": telefono,
            "trabajo": trabajo,
            "precio": precio,  
            "estado": estado,
            "cantidad": cantidad,
            "fecha_creacion": datetime.now().strftime("%d/%m/%Y"),
            "fecha_entrega_estimada": fecha_entrega_estimada,
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