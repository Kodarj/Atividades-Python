# Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

c = 0
while True:
    n = int(input('Digite o numero para saber a tabuada (NEGATIVO SE QUISER FINALIZAR): '))
    print('='*40)
    if n < 0:
        break
    for c in range (0,11):
        print(f'{n} X {c} = {n*c}')
        c += 1
    print('='*40)
print('TABUADA ENCERRADA!')