x = float(input('digite um número: '))
y = float(input('digite um número: '))
z = float(input('digite um número: '))
if x > y > z:
    print(f'o maior número é {x}!')
    print(f'o menor número é {z}!')
elif x > z > y:
    print(f'o maior número é {x}!')
    print(f'o menor número é {y}!')
elif y > x > z:
    print(f'o maior número é {y}!')
    print(f'o menor número é {z}!')
elif y > z > x:
    print(f'o maior número é {y}!')
    print(f'o menor número é {x}!')
elif z > x > y:
    print(f'o maior número é {z}!')
    print(f'o menor número é {y}!')
elif z > y > x:
    print(f'o maior número é {z}!')
    print(f'o menor número é {x}!')
