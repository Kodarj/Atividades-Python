# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números 
# e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

# biblioteca
from random import randint

# lista
num = list()

#Função
def valor():
    a = 0
    print('Sorteado os 5 valores da lista: ', end='')
    for c in range (0,5):
        a = randint(1,10)
        print(a, end=' ')
        num.append(a)
    print("FIM!")


def par(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print('Somando os valores pares de ', end='')
    for c in lista:
        print(c, end=' ')
    print(f', temos o numero {soma}')
    

#Programa

valor()
par(num)