from datetime import datetime

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

def pedir_texto(mensaje):
    while True:
        texto = input(mensaje)

        if texto.strip() == "":
            print("El valor no puede estar vacío.")
        else:
            return texto