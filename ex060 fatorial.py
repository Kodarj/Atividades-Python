# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

n1 = int(input('Digite um numero para calcular o fatorial: '))
total = 1
print(f'Calculando {n1}! = ', end='')
while n1 != 0:
    print(f'{n1}', end ='')
    print(' x ' if n1 > 1 else ' = ', end='')
    total = total * n1
    n1 -= 1
print(f'{total}')