# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = list()
while True:
    print('-'*40)
    i = int(input('Digite um valor: '))
    if i in valores:
        print('Esse valor já foi digitado')
        print()
    else:
        valores.append(i)
        print('Valor adicionado com sucesso...')
        print()
    resp = str(input('Quer continuar? ')).upper().strip()[0]
    if resp == 'N':
        break
    print()
print('-='*40)
print(f'Os valores em ordem crescente são: {sorted(valores)}')