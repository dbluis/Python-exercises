abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
       'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

noAbc = []

for index, i in enumerate(abc):
    if (index % 3) != 0:
        noAbc.append(i)

print(noAbc)
