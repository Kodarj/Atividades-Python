#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
print('='*30)
casa = float(input('Digite o valor do Imovél: R$ '))
sal = float(input('Digite o salário do comprador: R$ '))
ano = int(input('Digite em quantos anos quer pagar: '))
print('='*30)
#calculo
salp = sal * (30/100)
prest = casa / (ano * 12)
#comparação
if prest >= salp:
    print(f'Para pagar um imovél de R$ {casa:.2f} em {ano} anos, a prestação será de R$ {prest:.2f}.')
    print('!EMPRÉSTIMO NEGADO!')
else:
    print(f'Para pagar uma casa de R$ {casa:.2f} em {ano} a prestação será de R$ {prest:.2f}.')
    print('!EMPRÉSTIMO APROVADO!') 
   

