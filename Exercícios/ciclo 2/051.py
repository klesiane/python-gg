a1 = int(input('primeiro termo da P.A.? '))
r = int(input('razão da P.A.? '))
a10 = a1 + (10 - 1) * r
for c in range(a1, a10 + r, r):
    # pa = a1 + (c - 1) * r
    print(c)
