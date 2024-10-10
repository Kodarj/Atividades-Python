# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
from datetime import date
ano = int(input('Digite o Ano de nascimento do atleta: '))
atual = date.today().year

ano = atual - ano

if ano <= 9:
    print(f'O atleta Possui {ano} anos e está na categoria MIRIM')
elif 14 >= ano > 9:
    print(f'O atleta Possui {ano} anos e está na categoria INFANTIL')
elif 19 >= ano > 14:
    print(f'O atleta Possui {ano} anos e está na categoria JÚNIOR')
elif 25 >= ano > 19:
    print(f'O atleta Possui {ano} anos e está na categoria SÊNIOR')
else:
    print(f'O atleta Possui {ano} anos e está na categoria MASTER')
