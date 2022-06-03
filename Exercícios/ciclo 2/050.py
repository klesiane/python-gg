soma = 0
cont = 0
for c in range(1, 7):
    x = int(input('digite um número: '))
    if x % 2 == 0:
        soma = soma + x
        cont = cont + 1
print(f'você informou {cont} valor(es) par(es) e a soma é de {soma}')
