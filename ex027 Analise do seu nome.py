#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip()
nodiv = nome.split()
print(nodiv)
print(f'Seu primeiro nome é {nodiv[0]}')
print(f'Seu ultimo nome é {nodiv[len(nodiv)-1]}')
