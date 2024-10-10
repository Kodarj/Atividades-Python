# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
n = 0
for c in range(1,6):
    peso = float(input(f'Digite o peso da {c}º pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:    
        if peso > maior:
            maior = peso
            n = c
        if peso < menor:
            menor = peso
            n1 = c
print(f'O maior peso é de {maior}KG e foi da {n}º pessoa')
print(f'O menor peso é de {menor}KG e foi da {n1}º pessoa')