x = float(input('Qual a velocidade do seu carro em Km/h? '))
if x > 80:
    print('MULTADO! Você exedeu o limite que é 80Km/h')
    print(f'A multa vai custar: R${(x - 80)*7 :.2f} reais')
    print('Tenha um bom dia. Dirija com segurança!')
else:
    print('Tenha um bom dia. Dirija com segurança!')
