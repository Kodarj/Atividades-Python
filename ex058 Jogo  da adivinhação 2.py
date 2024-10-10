# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint
computador = randint(0,10)
tentativa = 1

resp = int(input('''Tente adivinhar o numero que eu pensei entre 0 e 10... 
'''))
while resp != computador:
    if resp > computador:
        print('Menos... Tente novamente.')
    elif resp < computador:
        print('Mais... Tente novamente.')
    tentativa += 1
    resp = int(input('Qual o seu novo palpite? '))
print()
print(f'ACERTOU! com {tentativa} tentativas. Parabéns!')