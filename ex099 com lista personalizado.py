# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

#biblioteca

from time import sleep

#lista
num = list()

#def
def val(mun):
    print('-='*40)
    maior = 0
    for c in mun:
        print(f'{c},' , end=' ', flush = True)
        sleep(1)
        if c > maior:
            maior = c
    print(f' Foram adicionados {len(mun)} numeros no total. ')
    print(f'O maior numero dessa sequencia é o {maior}.')
#programa

while True:
    num.clear()
    while True:
        print('-='*40)
        print()
        num.append(int(input('Digite um numero: ')))
        while True:
            r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
            if r not in 'SN':
                print('! DIGITE UMA RESPOSTA VÁLIDA !')
            else:
                break
        if r == 'N':
            break
        print()
    val(num) # Função
    print('-='*40)
    while True:
        q = str(input('Quer Fazer novamente? [S/N]: ')).upper().strip()[0]
        if q not in 'SN':
                print('! DIGITE UMA RESPOSTA VÁLIDA !')
        if q in 'SN':
            break
    if q == 'N':
        break
print('FIM DO PROGRAMA!')
