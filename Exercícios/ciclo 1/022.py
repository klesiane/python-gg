n = str(input('digite seu nome completo: ')).strip()
print('analisando seu nome...')
print(f'seu nome em letras maiúsculas é {n.upper()}')
print(f'seu nome em letras minúsculas é {n.lower()}')
print(f'seu nome ao todo tem {len(n)-n.count(" ")} letras')
print(f'seu primeiro nome tem {len(n.split()[0])} letras')
