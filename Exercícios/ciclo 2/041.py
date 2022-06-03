from datetime import date
a = int(input('qual ano você nasceu? '))
x = date.today().year
# x = int(input('qual ano você quer conferir? '))
if (x - a) <= 9:
    print('mirim')
elif 9 < (x - a) <= 14:
    print('infantil')
elif 14 < (x - a) <= 19:
    print('junior')
elif 19 < (x - a) <= 20:
    print('sênior')
elif (x - a) > 20:
    print('master')
