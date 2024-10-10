#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-='*20)
print(' '*20, end='')
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Digite o tamanho da primeira linha: '))
r2 = float(input('Digite o tamanho da segunda linha: '))
r3 = float(input('Digite o tamanho da terceira linha: '))

if r1+r2>r3 and r1+r3>r2 and r2+r3>r1:
    if r1 == r2 == r3:
        print('Formou um Triângulo Equilátero (com todos os lados iguais)')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('Formou um Triângulo Isósceles (com dois lados iguais apenas)')
    else:
        print('Formou um Triângulo Escaleno (Todos os lados com medidas distintas)')
else:
    print('Não formou um Triângulo')

