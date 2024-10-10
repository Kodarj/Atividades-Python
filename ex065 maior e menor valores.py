# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

fim = False
c = 0
soma = 0
while not fim:
    n = int(input('Digite um numero inteiro: '))
    c += 1
    soma += n
    if c == 1:
        menor = n
        maior = n
    if maior < n:
        maior = n
    if menor > n:
        menor = n
    r = str(input('Quer digitar mais um numero? ')).upper().strip()[0]
    if r == 'N':
        fim = True
print(f'''O maior número que digitou foi: {maior}
O menor número que digitou foi: {menor}
E a média dos {c} números é {soma/c}''')

