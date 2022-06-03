# jokenpô
from time import sleep
from random import randint
print('-=-' * 20)
print('VAMOS JOGAR JOKENPÔ???')
print('-=-' * 20)
sleep(1)
print('1 - pedra\n'
      '2 - papel\n'
      '3 - tesoura')
x = int(input('qual? (pedra, papel ou tesoura) '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
y = randint(1, 3)
print('-=-' * 20)
if x == 1 and y == 3:
    print('PARABÉNS!!! Você ganhou!')
    print('eu escolhi papel :(')
elif x == 1 and y == 2:
    print('HAHA! Eu ganhei!')
    print('eu escolhi papel :)')
elif x == 2 and y == 1:
    print('PARABÉNS!!! Você ganhou!')
    print('eu escolhi pedra :(')
elif x == 2 and y == 3:
    print('HAHA!Eu ganhei!')
    print('eu escolhi tesoura :)')
if x == 3 and y == 2:
    print('PARABÉNS!!! Você ganhou!')
    print('eu escolhi papel :(')
elif x == 3 and y == 1:
    print('HAHA!Eu ganhei!')
    print('eu escolhi pedra :)')
elif x == y:
    print('EMPATE!!')
print('-=-' * 20)
