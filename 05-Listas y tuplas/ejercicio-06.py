materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
reprobadas = []
for i in materias:
    nota = int(input(f"Cual fue su nota en la materia {i}: "))
    if nota < 6:
        reprobadas.append(i)

print(f"las materias que reprobadas son: {reprobadas}")
