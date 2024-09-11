v = [1, 2, 3]
u = [-1, 0, 2]

product = 0

for l1, l2 in zip(v, u):
    product += l1 * l2

print(f"El producto de las matrices v: ({v}) y ({u}) es de: {product}")
