num = [50, 75, 46, 22, 80, 65, 8]

minimo = maximo = num[0]
for x in num:
    minimo = min(x, minimo)
    maximo = max(x, maximo)

print(f"El numero max es: {maximo} y el min es {minimo}")
