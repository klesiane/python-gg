v = float(input('Valor da casa R$ '))
s = float(input('seu salário R$ '))
a = int(input('anos: '))
p = v / (a * 12)
if p > (30/100) * s:
    print('Sinto muito. Seu empréstimo não foi aprovado!')
else:
    print('Parabéns! Seu empréstimo foi aprovado!')
    print(f'Suas parcelas serão de R${p :.2f}')