# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

tot = 0
div = 0

val = int(input('Digite um numero inteiro: '))

for c in range(1,val + 1):
    if val % c == 0:
        print(f'\033[33m{c}\033[m', end=' ')
        tot = tot + 1
    else:
        print(f'\033[31m{c}\033[m', end=' ')
print()
print(f'O numero {val} foi divisivel {tot} vezes.')
if tot > 2:
    print(f'{val} não é um numero PRIMO')
else:
    print(f'{val} é um numero PRIMO!')