frase = str(input('digite uma frase: ')).strip().upper()
# separar as palavras p poder juntar elas sem espaço
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print(f'{frase.lower()} é um palíndromo!')
else:
    print(f'{frase.lower()} não é um palíndromo')
