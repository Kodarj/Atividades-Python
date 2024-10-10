# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. 
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[], [], []]

for c in range(0,3):
    matriz[0].append(int(input(f'Digite um valor para [0, {c}]: ')))
for c in range(0,3):
    matriz[1].append(int(input(f'Digite um valor para [1, {c}]: ')))
for c in range(0,3):
    matriz[2].append(int(input(f'Digite um valor para [2, {c}]: ')))
print('-='*40)
for c in matriz[0]:
    print(f'[{c:^5}]', end=' ')
print()
for c in matriz[1]:
    print(f'[{c:^5}]', end=' ')
print()
for c in matriz[2]:
    print(f'[{c:^5}]',end=' ')