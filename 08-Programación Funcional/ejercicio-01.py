def ApliDescuento(precio, descuento): return precio - (precio * descuento)/100


def AplicaIva(precio, iva): return precio + (precio * iva) / 100


print(ApliDescuento(1000, 20))
print(AplicaIva(1000, 20))

precios = {1000: 20, 5000: 10, 200: 50}

print({ApliDescuento(precio, iva) for precio, iva in precios.items()})
print({AplicaIva(precio, iva) for precio, iva in precios.items()})
