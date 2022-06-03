n1 = float(input('nota 1: '))
n2 = float(input('nota 2: '))
if (n1 + n2)/2 < 5:
    print('reprovado!')
elif 5 <= (n1 + n2)/2 <= 6.9:
    print('recuperação!')
elif (n1 + n2)/2 >= 7:
    print('aprovado! parabéns!!')
