# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista = list()
temp = list()

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    lista.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? ')).upper().strip()[0]
    print()
    if resp == 'N':
        break

print(f'{'No.':<4}{'NOME':<15}{'MÉDIA':>5}')
print('-'*30)

for c,p in enumerate(lista):
    print(f'{c:<4}{p[0]:<15}{(p[1] + p[2]) / 2:>5.1f}')


while True:
    print('-'*30)
    resp = int(input('Mostrar nota de qual aluno? (999 interrompe)'))
    if resp == 999:
        print('Finalizando....')
        break
    for c,p in enumerate(lista):
        if resp == c:
            print(f'As notas do {p[0]} foram: {p[1]}, {p[2]}')

print('Fim do Programa!')
