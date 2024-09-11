def MCD(num1, num2):
    a = set()
    b = set()
    for i in range(1, num1 + 1):
        x = num1 % i
        if x == 0:
            a.add(i)
    for y in range(1, num2 + 1):
        z = num2 % y
        if z == 0:
            b.add(y)
    return max(a.intersection(b))


def MCM(num1, num2):
    return (num1 * num2) / MCD(num1, num2)


print(MCD(24, 36))
print(MCM(24, 36))
