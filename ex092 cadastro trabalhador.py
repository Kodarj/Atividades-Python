# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

cadastro = dict()

while True:
    print('-='*40)
    
    cadastro['nome'] = str(input('Nome: '))
    nasc = int(input('Ano de nascimento: '))
    cadastro['idade'] = date.today().year - nasc
    cadastro['CTPS'] = int(input('Carteira de Trabalho (0 = não possui): '))
  
    if cadastro['CTPS'] != 0:
        cadastro['ano'] = int(input('Ano de contratação: '))
        cadastro['sal'] = float(input('Salário atual: R$'))
        cadastro['apo'] = (cadastro['ano'] + 35) - nasc
   
    print('-='*40)

#    for k,v in cadastro.items():
#        print(f'{k}: {v}') <- da pra fazer desse jeito porém vai puxar o nome das chaves do dicionário.

    print(f'Nome: {cadastro['nome']}')
    print(f'Idade: {cadastro['idade']}')
    print(f'CTPS : {cadastro['CTPS']}')
    
    if cadastro['CTPS'] != 0:
        print(f'Contratação: {cadastro['ano']}')
        print(f'Sálario: {cadastro['sal']}')
        print(f'Idade para se aposentar: {cadastro['apo']}')
   
    print('-='*40)
   
    resp = str(input('Repetir? ')).upper().strip()[0]
    
    if resp == 'N':
        break

print('>>>>> FIM DO PROGRAMA <<<<<')