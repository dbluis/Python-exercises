usuario = {"nombre": "", "edad": "", "dirección": "", "telefono": ""}

for x in usuario:
    usuario[x] = input(f"Escriba su {x}: ")

print(f"{usuario['nombre']} tiene {usuario["edad"]} años, vive en {
      usuario["dirección"]} y su telefono es: {usuario["telefono"]} ")
