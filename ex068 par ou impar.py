# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
c = 0
from random import randint
while True:
    comp = randint(1,10)
    print('-=-'*14)
    print('{:^40}'.format('PAR OU IMPAR'))
    print('-=-'*14)
    print()
    n = int(input('Digite um valor: '))
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou Impar? ')).upper().strip()[0]
    print('-'*25)
    soma = n + comp
    if soma % 2 == 0:
        print(f'Você escolheu {n} e o computador escolheu {comp}, deu {soma} E É PAR.')
        if pi == 'P':
            print('Você acertou!')
            c += 1
        else:
            print('Você errou!')
            break
    elif soma % 2 == 1:
        print(f'Você escolheu {n} e o computador escolheu {comp}, deu {soma} E É IMPAR')
        if pi == 'I':
            print('Você ganhou!')
            c += 1
        else:
            print('Você Perdeu!')
            break
print('-=-'*14)
print(f'GAME OVER! Você acertou {c} vezes consecutivas!')


