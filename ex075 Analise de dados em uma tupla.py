# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

list = (int(input('Digite o 1º numero: ')), int(input('Digite o 2º numero: ')), int(input('Digite o 3º numero: ')), int(input('Digite o 4º numero: ')))

print()
if 9 not in list:
    print ('Não tem o numero 9!')
else:
    print(f'o 9 aparece {list.count(9)} vezes!')
if 3 not in list:
    print('Não foi digitado nenhum 3')
else:
    print(f'O numero 3 foi digitado na posição {list.index(3)+1}')
print('Os numeros pares foi o ', end =' ')
for n in list:
    if n % 2 == 0:
        print(n, end=' ')


