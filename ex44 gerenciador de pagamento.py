# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros
r = True
while r == True:
    r = False
    print()
    print('{:=^40}'.format(' Lojas Ablueblue '))
    print()
    prod = float(input('Digite o valor do produto: R$'))
    print('''O PAGAMENTO SERA: 
               [1] A VISTA EM DINHEIRO/CHEQUE (10% DE DESCONTO)
               [2] A VISTA NO CARTÃO (5% DE DESCONTO)
               [3] 2X NO CARTÃO (PREÇO NORMAL)
               [4] 3X OU MAIS NO CARTÃO (20% DE JUROS)''')
    op = int(input('Escolha a forma de pagamento: '))
    if op == 1:
        print(f'O Valor do produto com 10% de desconto no dinheiro/Cheque será: R${prod-(prod*0.1):.2f}')
    elif op == 2:
        print(f'O Valor do produto com 5% de desconto no catão será: R${prod-(prod*0.05):.2f}')
    elif op == 3:
        print(f'Preço parcelado em 2x é: R${prod} , o valor de cada parcela sendo: R${prod/2:.2f}')
    elif op == 4:
        parc = int(input('Em quantas vezes será parcelado: '))
        print(f'O preço do produto com 20% de Juros fica R${prod+(prod*0.2):.2f} , e o valor de cada parcela fica: R${(prod+(prod*0.2))/parc:.2f}')
    else:
        print('Opção inválida, tente novamente')
    rep = str(input('Deseja fazer mais alguma operação? ')).lower()
    if (rep == 'sim') or (rep == 's'):
        r = True
print('FIM DO PROGRAMA!')
