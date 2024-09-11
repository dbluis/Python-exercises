renta = int(input("Escriba cuanto paga de renta anual: "))

if (renta > 60000):
    print("Tipo impositivo: 45%")
elif (renta <= 60000 and renta > 35000):
    print("Tipo impositivo: 30%")
elif (renta <= 35000 and renta > 20000):
    print("Tipo impositivo: 20%")
elif (renta <= 20000 and renta > 10000):
    print("Tipo impositivo: 15%")
else:
    print("Tipo impositivo: 5%")
