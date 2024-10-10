# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Digite o Sálario a ser calculado o aumento: R$'))

if sal > 1250:
    print(f'O aumento será de 10%, quem ganhava R${sal:.2f} , passa a ganhar R${sal+(sal*10/100):.2f}')
else:
    print(f'O aumento será de 15%, quem ganhava R${sal:.2f} , passa a ganhar R${sal+(sal*15/100):.2f}')