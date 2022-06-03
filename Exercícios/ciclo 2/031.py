x = float(input('Qual a distância da viagem em Km? '))
if x <= 200:
    print(f'A passagem vai custar: ${0.50 * x :.2f} reais')
else:
    print(f'A passagem vai custar: ${0.45 * x :.2f} reais')
