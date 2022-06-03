from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar..')
print('-=-' * 20)
x = int(input('Em que número eu pensei? '))
y = randint(0, 5)
print('PROCESSANDO....')
sleep(1)
if x == y:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {y} e não no {x}')
