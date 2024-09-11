divisa = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}

moneda = input("Escriba su divisa: ")

if moneda in divisa:
    print(f"Su divisa si se encuentra: {moneda}")
else:
    print("Su divisa no se encuentra")
