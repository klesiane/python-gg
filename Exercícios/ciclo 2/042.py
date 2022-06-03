print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
x = float(input('Primeiro segmento: '))
y = float(input('Segundo segmento: '))
z = float(input('Terceiro segmento: '))
if abs(y - z) < x < (y + z):
    print(f'é um triângulo!')
    if x == y == z:
        print('é um triângulo equilátero!')
    elif x == y or x == z or y == z:
        print('é um triângulo isóceles!')
    elif x != y != z != x:
        print('é um triângulo escaleno!')
else:
    print('não é um triângulo')
