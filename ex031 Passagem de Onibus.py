# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

#from time import sleep
#dis = float(input('Digite a distancia da viagem: '))
#if dis <= 200:
#    print('Abaixo ou igual de 200km o valor da passagem é R$0.50 por Km')
#    print('Calculando....')
#    sleep(3)
#    print(f'O valor da passagem é de R${dis*0.50:.2f}')
#else:
#    print('Acima de 200km o valor da passagem é R$0.45 por KM')
#    print('Calculando....')
#    sleep(3)
#    print(f'O valor da passagem é de R${dis*0.45:.2f}')

###########################

dis = float(input('Digite a distancia da viagem: '))
print(f'O valor da passagem é R${dis*0.50 if dis<=200 else dis*0.45:.2f}')