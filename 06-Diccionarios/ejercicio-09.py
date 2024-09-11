facturas = {}
continuar = ""
pagado = 0
pagar = 0
while continuar != "4":
    print("1-Añadir nueva factura \n2-Pagar una factura existente \n3-Mostrar facturas \n4-Terminar la operacion")
    continuar = input("Que operacion desea hacer: ")
    if continuar == "1":
        clave = input("Numero de la factura: ")
        valor = int(input("Valor de la factura: "))
        facturas[clave] = valor
        pagar += valor
    elif continuar == "2":
        clave = input("Escriba el numero de factura: ")
        pagado += facturas[clave]
        pagar -= facturas[clave]
        facturas.pop(clave)
    elif continuar == "3":
        print(facturas)

    print(f"Total a pagar: {pagar}")
    print(f"Total pagado: {pagado}")
