#Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).split()
fras = ''.join(frase).upper()
inverso = fras[::-1] #possivel apenas no python
'''for letra in range(len(fras) - 1, -1, -1):
    inverso += fras[letra]'''
print(f'O Inverso de {fras} é {inverso}')
if inverso == fras:
    print('Temos um palindromo!')
else:
    print('Não é um palindromo!')