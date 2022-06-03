d = int(input('dias com o carro: '))
k = float(input('km rodados: '))
v = (60 * d) + (0.15 * k)
print(f'preço a pagar é: {v :.2f}')

# lembrando que esse " :.2f " serve p escolher a qnt de digito que aparece depois da virgula
