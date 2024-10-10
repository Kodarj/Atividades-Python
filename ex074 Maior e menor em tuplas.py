# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

val = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0, 10))
print(f'Os valores sorteados são: {val}')
# val = sorted(val)
# print(f'O maior valor é {val[-1]}')
# print(f'O menor valor é {val[0]}')
print(f'O maior valor sorteado foi {max(val)}')
print(f'O menor valor sorteado foi {min(val)}')