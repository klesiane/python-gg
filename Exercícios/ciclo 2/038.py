x = int(input('valor do primeiro número: '))
y = int(input('valor do segundo número: '))
if x > y:
    print(f'{x} é maior que {y}')
elif x < y:
    print(f'{y} é maior que {x}')
else:
    print(f'{x} e {y} são iguais')
