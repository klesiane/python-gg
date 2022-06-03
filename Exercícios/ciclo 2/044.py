print('\033[1;34m-=-\033[m' * 20)
v = float(input('\033[1;36mqual o valor do produto? \033[m'))
print('\033[1;34m-=-\033[m' * 20)
print('1 - à vista (dinheiro/cheque): 10% de desconto\n'
      '2 - à vista no cartão: 5% de desconto\n'
      '3 - em até 2x no cartão: preço normal\n'
      '4 - 3x ou mais no cartão: 20% de juros')
p = int(input('\033[1;36mqual a forma de pagamento? \033[m'))
print('\033[1;34m-=-' * 20)
if p == 1:
    print(f'o valor de pagamento será R${90 / 100 * v}')
elif p == 2:
    print(f'o valor de pagamento será R${95 / 100 * v}')
elif p == 3:
    print(f'o valor de pagamento será R${v}')
elif p == 4:
    print(f'o valor de pagamento será R${120 / 100 * v}')
