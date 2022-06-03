x = int(input('digite um número: '))
print('- 1 para binário')
print('- 2 para octal')
print('- 3 para hexadecimal')
c = int(input('qual a base de conversão? '))
if c == 1:
    print(f'{x} convertido para binário é igual a {bin(x)[2:]}')
elif c == 2:
    print(f'{x} convertido para octal é igual a {oct(x)[2:]}')
elif c == 3:
    print(f'{x} convertido para hexadecimal é igual a {hex(x)[2:]}')
else:
    print('opção inválida')
