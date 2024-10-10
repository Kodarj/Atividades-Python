# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe o seu sexo [M/F]: ')).upper().strip()[0] # fatiamento para pegar a primeira letra
'''while (sexo != 'M') and (sexo != 'F'):''' # Meu jeito
while sexo not in 'MmFf': #jeito guanabara
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [M/F]: ')).upper().strip()[0]
print(f'Sexo {sexo} registrado com sucesso.')