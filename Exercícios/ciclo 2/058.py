from random import randint
from time import sleep
cont = 0
print('\033[33m-=-' * 20)
print('\033[mVou pensar em um número entre 0 e 10. Tente advinhar..')
print('\033[33m-=-' * 20)
x = int(input('\033[mEm que número eu pensei? '))
y = randint(0, 10)
print('\033[037mPROCESSANDO....')
sleep(1)
if x == y:
    print('\033[35mPARABÉNS! Você conseguiu me vencer!\033[m')
else:
    print(f'\033[31mGANHEI! Eu pensei no número {y} e não no {x}\033[m')
    while x != y:
        cont = cont + 1
        print('\033[33m-=-' * 20)
        print('\033[mVou pensar em um número entre 0 e 10 novamente. Tente advinhar..')
        print('\033[33m-=-' * 20)
        x = int(input('\033[mEm que número eu pensei agora? '))
        y = randint(0, 10)
        print('\033[037mPROCESSANDO....')
        sleep(1)
        if x != y:
            print(f'\033[31mAinda não foi dessa vez! Eu pensei no número {y} e não no {x}')
    if x == y:
            print(f'\033[35mParabéns! No entanto você precisou de {cont} tentativas.')
