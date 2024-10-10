#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
from time import sleep
from random import choice
n0 = 'PEDRA'
n1 = 'PAPEL'
n2 = 'TESOURA'
lista = [n0,n1,n2]
escolha = choice(lista)
print()
print('{:=^40}'.format(' JOKENPO '))
print()
jog = str(input(''' ESCOLHA UMA OPÇÃO:
                - PEDRA
                - PAPEL
                - TESOURA
                ESCOLHA A OPÇÃO: ''')).upper()
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!')
print('-=-'*20)
print(f'''O Computador escolheu {escolha} 
O Jogador escolheu {jog}''')
print('-=-'*20)
if (jog == 'PEDRA' and escolha == n0) or (jog == 'PAPEL' and escolha == n1) or (jog == 'TESOURA' and escolha == n2):
    print('EMPATE')
elif (jog == 'PEDRA' and escolha == n1) or (jog == 'PAPEL' and escolha == n2) or (jog == 'TESOURA' and escolha == n0):
    print('Voce Perdeu!')
elif (jog == 'PEDRA' and escolha == n2) or (jog == 'PAPEL' and escolha == n0) or (jog == 'TESOURA' and escolha == n1):
    print('Você Ganhou!')
else:
    print('Escolha uma opção válida!')