# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
sair = False
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

while not sair:
    print('-==-'*20)
    print('Escolha a operação desejada:')
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NÚMEROS')
    print('[5] SAIR DO PROGRAMA')
    op = int(input('DIGITE A OPÇÃO DESEJADA: '))
    print('-==-'*20)
    if op == 1:
        print(f'O resultado da soma de {n1} + {n2} é de {n1+n2}')
    elif op == 2:
        print(f'O resultado da multiplicação de {n1} X {n2} é de {n1*n2}')
    elif op == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        elif n1 == n2:
            print('Os numeros são iguais')
        else:
            print(f'{n2} é maior que {n1}')
    elif op == 4:
        n1 = int(input('Digite o Primeiro novo valor: '))
        n2 = int(input('Digite o Segundo novo valor: '))
    elif op == 5:
        sair = True
        print('Finalizando...')
    else:
        print('Por favor, digite uma opção VÁLIDA!')
    sleep(2)
print('FIM DO PROGRAMA!')