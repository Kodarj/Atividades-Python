# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogadas = dict()
ranking = list()

print('---------- VALORES SORTEADOS ----------')
n = int(input('Quantos jogadores irão jogar? '))
print('-='*30)

for c in range(1,n+1):
    sleep(1)
    jogadas[f'jogador {c}'] = randint(1,6)
    print(f'Jogador {c} tirou {jogadas[f'jogador {c}']} no dado.')

ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True) # o () depois de itemgetter é para escolher qual chave é para dar sorted. E no final sempre vai ser lista.

print('-='*30)
print(' == RANKING DOS JOGADORES == ')

for i,v in enumerate(ranking):
    sleep(1)
    print(f'{i+1}º LUGAR: {v[0]} com {v[1]}.')
print('-='*30)
