n = int(input('digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        tot = tot + 1
        print(f'\033[33m{c}', end=' ')
    else:
        print(f'\033[31m{c}', end=' ')
if tot == 2:
    print(f'\n\033[m{n} é um número primo!')
else:
    print(f'\n\033[m{n} não é um número primo!')
