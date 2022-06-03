sexo = str(input('qual seu sexo?[F/M] ')).strip().upper()
while sexo not in 'MmFf':
    sexo = str(input('dados inválidos. por favor, informe o seu sexo[F/M]: ')).strip().upper()
print(f'sexo {sexo} registrado com sucesso!')