# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
maior = 0
menor = 0
iddtot = 0

for c in range(1,5):
    print()
    print(f'-------- {c}º Pessoa -------')
    nome = str(input('Nome: ')).strip()
    sexo = str(input('Sexo (M ou F): ')).upper().strip()
    idade= int(input('Idade: '))
    if (sexo == 'M') and idade > maior:
        nomeH = nome
        maior = idade
        iddmai = idade
    if (sexo == 'F') and idade < 20: 
        menor = menor + 1
    iddtot = iddtot + idade
print('-'*15)
print(f'O Nome do homem mais velho é {nomeH} e ele tem {iddmai} anos.')
print(f'No total {menor} mulheres tem menos de 20 anos')
print(f'A média de idade do grupo é de {iddtot / 4:.1f}')