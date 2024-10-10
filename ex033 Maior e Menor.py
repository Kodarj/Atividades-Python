# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
#Validando o MENOR
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#Validando o MAIOR
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O MAIOR é {maior} e o MENOR é {menor}')

#########################################################
#if n1 > n2 and n2 > n3:
#    print(f'O MAIOR numero é o {n1} e o MENOR é {n3}')
#elif n1 > n3 and n3 > n2:
#    print(f'O MAIOR numero é o {n1} e o MENOR é {n2}')
#elif n2 > n1 and n1 > n3:
#    print(f'O MAIOR numero é o {n2} e o MENOR é {n3}')
#elif n2 > n3 and n3 > n1:
#    print(f'O MAIOR numero é o {n2} e o MENOR é {n1}')
#elif n3 > n1 and n1 > n2:
#    print(f'O MAIOR numero é o {n3} e o MENOR é {n2}')
#elif n3 > n2 and n2 > n1:
#    print(f'O MAIOR numero é o {n3} e o MENOR é {n1}')