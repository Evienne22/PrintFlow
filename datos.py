import json

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
    
    except json.JSONDecodeError:
        print("Error: el archivo clientes_archivados.json está dañado.")
        return []

def guardar_clientes_archivados(clientes_archivados):
    with open("clientes_archivados.json", "w") as archivo:
        json.dump(clientes_archivados, archivo, indent=4)
        
def guardar_clientes(clientes):
    with open("clientes.json", "w") as archivo:
        json.dump(clientes, archivo, indent=4)