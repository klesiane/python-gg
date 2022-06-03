x = int(input('Digite um ano: '))
if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
    print('é um ano bissexto!')
else:
    print('não é um ano bissexto')
