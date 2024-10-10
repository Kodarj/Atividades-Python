# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
for c in range(1,7):
    v = int(input('Digite um valor: '))
    if v % 2 == 0:
        soma = soma + v
print(f'O Valor das somas dos numeros pares é de: {soma}')