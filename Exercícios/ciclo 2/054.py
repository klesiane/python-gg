from datetime import date
hoje = date.today().year
cont = 0
cont2 = 0
for c in range(1, 8):
    x = int(input('qual seu ano de nascimento? '))
    idade = hoje - x
    if idade >= 21:
        cont2 = cont2 + 1
    else:
        cont = cont + 1
print(f'há {cont} pessoa(s) menor(es) de idade')
print(f'há {cont2} pessoa(s) maior(es) de idade')
