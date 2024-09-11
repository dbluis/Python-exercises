datos = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
datos = datos.split("\n")

titulos = datos[0].split(";")

datos.remove(datos[0])

clientes = {}
for x in datos:
    x = x.split(";")
    cliente = {}
    for i in range(len(titulos)):
        if titulos[i] == "nif":
            clientes[x[i]] = cliente
        else:
            cliente[titulos[i]] = x[i]

print(clientes)
