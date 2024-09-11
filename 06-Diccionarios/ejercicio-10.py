clientes = {}
continuar = ""

while continuar != "6":
    print("Opciones:\n(1) Añadir cliente \n(2) Eliminar cliente \n(3) Mostrar cliente \n(4) Listar todos los clientes \n(5) Listar clientes preferentes \n(6) Terminar ")
    continuar = input("Escoja una opcion: ")
    if continuar == "1":
        nif = int(input("Escriba el nif del cliente: "))
        cliente = {"nombre": "", "dirección": "",
                   "teléfono": "", "correo": "", "preferente": ""}
        for i in cliente:
            cliente[i] = input(f"Escriba {i}: ")
        clientes[nif] = cliente
    elif continuar == "2":
        nif = input("Escriba el nif del cliente a eliminar: ")
        clientes.pop(nif)
    elif continuar == "3":
        nif = int(input("Escrbia el nif del cliente que quiere ver: "))
        if nif in clientes:
            print('NIF:', nif)
            for clave, valor in clientes[nif].items():
                print(clave.title() + ':', valor)
        else:
            print('No existe el cliente con el nif', nif)
    elif continuar == "4":
        for i in clientes:
            print(f"NIF: {i} Nombre: {clientes[i]["nombre"]}")
    elif continuar == "5":
        print("Clientes preferentes")
        for i in clientes:
            if clientes[i]["preferente"] == "si":
                print(f"NIF: {i} y Nombre: {clientes[i]["nombre"]}")
