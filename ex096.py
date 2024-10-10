# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

#Função
def area(larg, comp):
    print()
    print(f'A área de um terreno {larg}x{comp} é de {larg*comp:.1f} m²')
    print('-'*30)


# Programa real
print(' CONTROLE DE TERRENOS')
print('-'*30)
a = float(input('LARGURA [M]: '))
b = float(input('COMPRIMENTO [M]: '))
area(a,b)