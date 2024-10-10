# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

maior = 0
menor = 0

atual = date.today().year
for c in range (1,8):
    idd = int(input(f'Digite o ano de nascimento da {c}º pessoa: '))
    if atual - idd >= 21:
        maior = maior + 1
    else:
        menor = menor + 1
print(f'No total, {maior} de pessoas são maiores de idade e {menor} são menores de idade')