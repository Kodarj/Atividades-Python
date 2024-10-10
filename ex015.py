#Escreva um programa que pergunte a quantidade de Km percorridos por
#um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado

print('='*49)
print('='*15,end=' ')
print('Aluguel de Carros',end=' ')
print('='*15)
print('KM = R$0.15',end='               ')
print('Dia = R$60 ')
print('='*49)
km = float(input('Quantos KM percorridos: '))
d = int(input('Por quantos dias o carro foi alugado: '))

print(f'Total a pagar: R${(km*0.15)+(d*60):.2f}')

print('='*49)