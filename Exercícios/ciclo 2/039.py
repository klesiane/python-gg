from datetime import date
x = date.today().year
a = int(input('qual ano você nasceu? '))
# x = int(input('qual ano você quer conferir? '))
if x - a == 18:
    print('já está na hora de se alistar')
elif x - a < 18:
    print(f'falta {18 - (x - a)} ano(s) para se alistar')
else:
    print(f'já se passou {(x - a) - 18} ano(s) desde que você deveria ter alistado')
