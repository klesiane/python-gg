import random
n1 = input('primeiro aluno: ')
n2 = input('segundo aluno: ')
n3 = input('terceiro aluno: ')
n4 = input('último aluno: ')
lista = [n1, n2, n3, n4]
print(f'o aluno escolhido foi: {random.choice(lista)}')
