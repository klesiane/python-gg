import math
x = float(input('número em graus: '))
cos = math.cos(math.radians(x))
sen = math.sin(math.radians(x))
tang = math.tan(math.radians(x))
print(f'o número {x} tem como cosseno: {cos :.2f}\n'
      f'o número {x} tem como seno: {sen :.2f}\n'
      f'o número {x} tem como tangente {tang :.2f}\n')
