# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
n50 = n20 = n10 = n1 = 0
print("="*30)
print('{:^25}'.format(' BANCO GORDO '))
print('='*30)
valor = int(input('Digite o valor a ser sacado: R$'))


while True:
    if valor < 20:
        break
    valor -= 20
    n20 += 1
while True:
    if valor < 10:
        break
    valor -= 10
    n10 += 1
while True:
    if valor < 1:
        break
    valor -= 1
    n1 += 1
print('='*30)
if n50 != 0:
    print (f'Total de {n50} cédulas de R$50')
if n20 != 0:
    print(f'Total de {n20} cédulas de R$20')
if n10 != 0:
    print(f'Total de {n10} cédulas de R$10')
if n1 != 0:
    print(f'Total de {n1} cédulas de R$1')
print('='*30)
print('Obrigado e volte sempre!')
