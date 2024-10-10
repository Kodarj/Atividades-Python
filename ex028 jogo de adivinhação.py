# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from time import sleep
from random import randint
f = True
while f == True:
    f = False
    print('-=-'*50)
    print('Vou pensar em um número entre 0 e 5. tente adivinhar...')
    print('-=-'*50)
    print('')
    n = int(input('Em qual número eu pensei? ')) #Jogador adivinhando
    print('PROCESSANDO...')
    sleep(3)
    r = randint(0,5) # COmputador pensa no numero
    if n == r: # resultado
        print('PARABÉNS! Você acertou!')
    else:
        print(f'Que pena, você errou! Era o número {r}')
    res = str(input('Quer jogar novamente? ')).strip().upper()
    if (res == 'SIM' or res == 'S'):
        f = True
print('Obrigado por jogar!')
