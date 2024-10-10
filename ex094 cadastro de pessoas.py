# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
# No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média

registro = list()
cadastro = dict()
tot = 0

# leitura de dados

while True:
    print('-='*40)
    cadastro['Nome'] = str(input('Nome: '))
    
    while True:
        cadastro['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if cadastro['sexo'] in 'MF':
            break
        print('------ Digite uma opção válida digite apenas M ou F ------')
    
    cadastro['idade'] = int(input('Idade: '))
    registro.append(cadastro.copy())
   
    while True:
        resp = str(input('Quer continuar? ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('------ Responda apenas Sim ou Não------')
   
    if resp == 'N':
        break

# processamento

print('-='*40)
print(f'- O total de pessoas cadastradas foram de {len(registro)}')
print('-='*40)

for c in registro:
    tot += c['idade'] # aqui uso a chave "idade" para puxar de dentro da lista REGISTRO a idade que eesta em cada dicionario

print(f'- A média das idades é de {tot / len(registro):.0f}')
print('-='*40)
print('- As mulheres cadastradas foram: ',end='')

for c in registro:
    if c['sexo'] == 'F':
        print(f'{c["Nome"]}', end=', ')

print()
print('-='*40)
print('- Pessoas com idade acima da média: ')

for c in registro:
    if c['idade'] >= tot / len(registro):
        print('     ')
        for k, v in c.items():
            print(f'{k} = {v};', end='  ')
print()
print('-='*40)