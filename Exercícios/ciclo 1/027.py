n = str(input('digite seu nome completo: ')).strip()
print(f'seu primeiro nome é {n.split()[0]}')
print(f'seu último nome é {n.split()[len(n)-1]}')
