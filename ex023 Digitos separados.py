#Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

valor = int(input('Digite o valor: '))
u = valor // 1 % 10
d = valor // 10 % 10
c = valor // 100 % 10
m = valor // 1000 % 10

print( f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'centena: {c}')
print(f'milhar: {m}')