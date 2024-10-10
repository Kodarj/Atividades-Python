#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um numéro: '))
print('='*25)
print('''Digite a opção desejada para conversão:
[1] Binário
[2] Octal
[3] Hexadecimal''')
op = int(input('Sua opção: '))
#resolução
if op == 1:
    print(f'O valor em binário de {num} é {bin(num)[2:]}')
elif op == 2:
    print(f'O valor em Octal de {num} é {oct(num)[2:]}')
elif op == 3:
    print(f'O valor em Hexadecimal de {num} é {hex(num)[2:]}')
else:
    print('Digite um valor válido.')

