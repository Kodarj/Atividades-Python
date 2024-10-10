# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

# importar biblioteca

from time import sleep

# Função
def lin():
    print('-='*40)


def contador():
    lin()
    print('Contagem de 1 até 10 de 1 em 1:')
    for h in range (1,11,1):
        sleep(0.6)
        print(h, end='')
        print(', ', end='')
    print('FIM!')
    lin()
    print('Contagem de 10 até 0 de 2 em 2:')
    for h in range(10,-2,-2):
        sleep(0.6)
        print(h, end='')
        print(', ', end='')
    print('FIM!')
    lin()
    print('Agora é a sua vez de personalizar a contagem!')
    a = int(input('Inicio: '))
    b = int(input('Fim: '))
    c = int(input('Passo: '))
    lin()
    if c == 0:
        if a > b:
            print(f'Contagem de {a} até {b} de 1 em 1:')
            for d in range (a,b-1,-1):
                sleep(0.6)
                print(d, end='')
                print(', ', end='')
            print('FIM!')
        elif b > a:
            print(f'Contagem de {a} ate {b} de 1 em 1:')
            for d in range (a,b+1,1):
                sleep(0.6)
                print(d, end='')
                print(', ', end='')
            print('FIM!')
    elif a < b:
        print(f'Contagem de {a} até {b} de {c} em {c}:')
        for d in range(a,b+c,c):
            sleep(0.6)
            print(d, end='')
            print(', ', end='')
        print('FIM!')
    elif a > b:
        print(f'Contagem de {a} ate {b} de {c} em {c}: ')
        for d in range (b,a+c,c):
            sleep(0.6)
            print(d, end='')
            print(', ', end='')
        print('FIM!')
    lin()

    
# Programa

print()
contador()