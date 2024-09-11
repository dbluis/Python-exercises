password = input("Introduzca una contraseña: ")

while True:
    password2 = input("Introduzca la contraseña: ")
    if password == password2:
        print("Bienvenido!")
        break
    else:
        print("Contraseña incorrecta")
