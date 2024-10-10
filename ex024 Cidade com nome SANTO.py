# Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

nome = str(input('Digite o nome da Cidade em que nasceu: ')).strip()
print (nome[:5].upper() == 'SANTO')