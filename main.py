clientes = []
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
        clientes.append(nombre)
        print()
        print("Cliente registrado correctamente.")
        
    elif opcion == "2":
        print()
        print("Lista de clientes:")
        for cliente in clientes:
            print("- " + cliente)
    elif opcion == "3":
        print("Cerrando el PrintFlow.")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")