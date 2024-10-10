# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados. 
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

num = list()
while True:
    num.append(int(input('Digite um valor: ')))
    res = str(input('Quer continuar? ')).upper().strip()[0]
    if res == 'N':
        break
    print('-'*40)
print()
print(f'A quantidade de numeros digitados foram de: {len(num)}')
print()
num.sort(reverse=True)
print(f'A lista de valores em ordem decrescente é: {num}')
print()
if 5 in num:
    print('O valor 5 foi digitado.')
else:
    print('O valor 5 não foi digitado!')