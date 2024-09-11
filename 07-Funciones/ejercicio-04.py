def factura(num, iva=21):
    return num + (num * iva)/100


print(factura(1000, 10))
print(factura(1000))
