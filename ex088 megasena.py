# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
jogo = list()
lista = list()
print('-'*40)
print('           JOGO DA MEGASENA                  ')
print('-'*40)
print()
n = int(input('Quantos jogos deseja gerar? '))
print()

for c in range (0,n):
    for i in range (0,6):
        num = randint(1,60)
        if num not in jogo:
            jogo.append(num)
    jogo.sort()
    lista.append(jogo[:])
    jogo.clear()
print('-='*3, f'SORTEANDO {n} JOGOS', '-='*3)

for p in lista:
    sleep(1)
    print(p)
    print()

print('-='*16)