# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:     
# A) Quantas pessoas foram cadastradas.          
# B) Uma listagem com as pessoas mais pesadas.                                                                                                 
# C) Uma listagem com as pessoas mais leves.
cadastros = list()
ficha = list()
menor = 0
maior = 0
while True:
    ficha.append(str(input('Nomes: ')))
    ficha.append(float(input('Peso: ')))
    if len(cadastros) == 0:
        menor = maior = ficha[1]
    else: 
        if ficha[1] > maior:
            maior = ficha[1]
        elif ficha[1] < menor:
            menor = ficha[1]
    cadastros.append(ficha[:])
    ficha.clear()
    res = input('Quer continuar? ').upper().strip()[0]
    if res == 'N':
        break
    
print(f'Foi cadastrado um total de {len(cadastros)} pessoas.')
print(f'O maior peso registrado foi de {maior} KG. Peso de ', end=' ')
for p in cadastros:
    if p[1] == maior:
        print(p[0], end=', ')
print()
print(f'O menor peso registrado foi {menor} KG. Peso de ', end=' ')
for p in cadastros:
    if p[1] == menor:
        print(f'[{p[0]}', end=' ')
