# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

par = list()
impar = list()
num = list()

while True:
    num.append(int(input('Digite um valor: ')))
    print()
    res = str(input('Quer Continuar? ')).upper().strip()[0]
    if res == 'N':
        break
    print('-'*40)
for c in num:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'A lista que foi digitada: {num}')
print()
print(f'os valores pares foram: {par}')
print()
print(f'Os valores impares foram: {impar}')