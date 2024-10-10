# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print('-=-'*15)
print('{:^40}'.format('Progressão Aritmética'))
print('-=-'*15)
print()

v = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
for c in range(1,11):
    print(f'{v}', end=' -> ')
    v = v + r
print('ACABOU!')