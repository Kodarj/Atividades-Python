# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
soma = 0
c = 0
n = 0
while n != 999:
    soma += n
    n = int(input('Digite o valor inteiro (digite 999 para parar): '))
    if n != 999:
        c += 1
print(f'''A quantidade de numeros digitados foi de: {c}
A soma de todos os valores é de {soma}''')
