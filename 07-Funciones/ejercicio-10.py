def to_binario(num):
    binario = []
    while num != 0:
        binario.append(str(num % 2))
        num = num // 2
    binario.reverse()
    return "".join(binario)


def to_decimal(binario):
    num = 0
    for i in range(len(binario)):
        num += int(binario[i]) * 2 ** (len(binario) - (i + 1))
    return num


print(to_binario(11))
print(to_decimal("1011"))
