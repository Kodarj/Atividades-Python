# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
atual = date.today().year
sexo = input('Você é homem ou mulher? ').lower()
if sexo == 'homem':
    idade = int(input('Digite a idade da pessoa: '))

    if idade < 18:
        print(f'Ainda falta {18 - idade} anos para se alistar.')
        print(f'Seu alistamento será em {atual + (18 - idade)}')
    elif idade == 18:
        print('Está na hora de se alistar')
    else:
        print(f'Já passou {idade - 18} anos da idade de se alistar')
        print(f'Seu alistamento era pra ser feito em {atual - (idade - 18)}')
else:
    print('Você não precisa fazer o alistamento, apenas homens são obrigados.')