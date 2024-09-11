notas = {"matematica": 5, "lengua": 6, "histoira": 8}

rt = {materia.capitalize(): nota for (materia, nota) in notas.items()}

print(rt)


def grade(score):

    if score < 5:
        return "mal"
    elif score < 7:
        return "Regular"
    elif score < 9:
        return "Muy bien"
    elif score <= 10:
        return "Exelente"
    else:
        return "Ingrese una nota valida"


def apply_grades(scores):

    subjects = map(str.upper, scores.keys())
    grades = map(grade, scores.values())
    return dict(zip(subjects, grades))


print(apply_grades({'Matemáticas': 6.5, 'Física': 5, 'Química': 3.4,
      'Economía': 8.2, 'Historia': 9.7, 'Programación': 10}))
