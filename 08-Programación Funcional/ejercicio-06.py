def grade(score):

    if score < 5:
        return "Bad"
    elif score < 7:
        return "Regular"
    elif score < 9:
        return "Muy bien"
    elif score < 10:
        return "Exelente"
    else:
        return "Ingrese una nota valida"


def apply_grade(scores):

    return list(map(grade, scores))


print(apply_grade([5, 7, 8, 1, 2, 3.5, 6, 8, 9]))
