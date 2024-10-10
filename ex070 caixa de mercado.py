# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

prodmil = total = menor = 0
barato = ''

while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$ '))
    total += preco
    if total == preco or preco < menor:
        menor = preco
        barato = nome
    if preco >= 1000:
        prodmil += 1
    res =''
    if res != 'SN':
        res = str(input('Fazer novamente? ')).upper().strip()[0]
    if res == 'N':
        break
print()
print(f''' Total da compra: R${total}
Total de produtos custando mais que R$1000,00: {prodmil}
Nome do produto mais barato: {barato} custando R$ {menor}''')
print('{:-^40}'.format(' FIM DO PROGRAMA '))