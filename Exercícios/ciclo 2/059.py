print('-=-' * 20)
print(' ' * 22, end='')
print('CALCULADORA')
print('-=-' * 20)

x = int(input('primeiro valor: '))
y = int(input("segundo valor: "))

escolha = 0
while escolha != 5:
    print('\n[ 1 ] somar \n'
          '[ 2 ] multiplicar \n'
          '[ 3 ] comparar qual é maior \n'
          '[ 4 ] novos números \n'
          '[ 5 ] sair do programa')
    print('-=-' * 20)
    escolha = int(input('por favor escolha uma das opções acima: '))
    print('-=-' * 20)
    if escolha == 1:
        print(f'{x} + {y} = {x + y}')
    elif escolha == 2:
        print(f'{x} * {y} = {x * y}')
    elif escolha == 3:
        if x > y:
            print(f'{x} é maior que {y}')
        elif x < y:
            print(f'{y} é maior que {x}')
        else:
            print(f'{x} e {y} são iguais')
    elif escolha == 4:
        x = int(input('primeiro valor: '))
        y = int(input('segundo valor: '))
    elif escolha == 5:
        print('finalizando...')
    else:
        print('opção inválida. tente novamente')
    print('-=-' * 20)
print('fim do programa! volte sempre!')
