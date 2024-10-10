# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

p = h = m = 0
while True:
    print('-'*40)
    idd = int(input('Digite a idade da pessoa: '))
    sexo = res = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo da pessoa: ')).upper().strip()[0]
    if idd > 18:
        p += 1
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idd < 20:
        m += 1
    while res not in 'SN':    
        res = str(input('Quer fazer mais um cadastro? ')).upper().strip()[0]
    if res == 'N':
        break
print('-=-'*20)
print(f'''A quantidade de pessoas com mais de 18 anos é: {p}
A quantidade de homens cadastrados é de : {h}
A quantidade de mulheres com menos de 20 anos é de: {m}''')
print('-=-'*20)