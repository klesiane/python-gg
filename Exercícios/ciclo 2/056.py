soma = 0
média = 0
nhomem = ''
mhomem = 0
totmulhoer20 = 0
# nome do homem mais velho
# idade do homem mais velho
for p in range(1, 5):
    nome = str(input('seu nome: '))
    idade = int(input('sua idade: '))
    sexo = str(input('sexo [F/M]: ')).strip().upper()
    print('-=-' * 20)
    soma = soma + idade
    if p == 1 and sexo in 'Mm':
        mhomem = idade
        nhomem = nome
    if sexo in 'Mm' and idade > mhomem:
        mhomem = idade
        nhomem = nome
    if sexo in 'Ff' and idade < 20:
        totmulhoer20 = totmulhoer20 + 1

média = soma / 4
print(f'a média das idades do grupo é {média} anos')
print(f'o homem mais velho se chama {nhomem} e tem {mhomem} anos')
print(f'há {totmulhoer20} mulheres com menos de 20 anos')
