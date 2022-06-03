print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
x = float(input('Primeiro segmento: '))
y = float(input('Segundo segmento: '))
z = float(input('Terceiro segmento: '))
if abs(y - z) < x < (y + z):
    print(f'é um triângulo!')
else:
    print('não é um triângulo')
