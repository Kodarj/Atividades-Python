from random import shuffle

n1 = input('Digite o nome do Aluno: ')
n2 = input('Digite o nome do Aluno: ')
n3 = input('Digite o nome do Aluno: ')
n4 = input('Digite o nome do Aluno: ')
lista = [n1,n2,n3,n4]
shuffle(lista)
print(f'A ordem de apresentação sera:{lista}')