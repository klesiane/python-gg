a = float(input('qual sua altura (em m)? '))
p = float(input('qual seu peso (em Kg)? '))
imc = p / a ** 2
if imc < 18.5:
    print('você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('peso ideal!')
elif 25 <= imc < 30:
    print('sobrepeso!')
elif 30 <= imc < 40:
    print('obesidade!')
elif imc >= 40:
    print('obesidade mórbida!')
