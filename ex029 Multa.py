#  Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#  A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Digite a velocidade do veiculo: '))
if vel > 80:
    vel = (vel - 80)*7
    print('MULTADO! Você excedeu o limite permitido de 80 Km/h')
    print(f'Você deve pagar uma multa de R${vel:.2f}!')
else:
    print('Esta na velocidade permitida!')
print('Tenha uma boa viagem!')
