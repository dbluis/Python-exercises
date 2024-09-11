materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

nota = []

for m in materias:
    n = int(input(f"Escriba la nota de la materia {m}: "))
    nota.append(n)

for j, i in zip(materias, nota):
    print(f"En la materia {j} la nota es {i}")
