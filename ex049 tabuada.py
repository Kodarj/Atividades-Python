# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

v = int(input('Digite o valor que quer saber a tabuada: '))
for c in range (0,11):
    print(f'{v} X {c} = {v*c}')
    print()
print('Fim da tabuada!')