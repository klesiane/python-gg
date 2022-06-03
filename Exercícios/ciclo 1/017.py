ca = float(input('cateto adjascente: '))
co = float(input('cateto oposto: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'o valor da hipotenusa é : {hi :.2f}')

#or 'hi = math.hypot(co, ca)' and "import math"