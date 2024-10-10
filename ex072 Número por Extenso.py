# Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numero = ('zero', ' um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
          'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
res = ' '
while res not in 'N':
    res = ' '
    while True:
        dig = int(input('Digite um numéro de 0 a 20: '))
        if 0 <= dig <= 20:
            break
        print('Valor incorreto. Tente novamente.', end=' ')
    print()
    print(f'O valor que você digitou foi de {numero[dig]}')
    while res not in 'SN':
        res = str(input('Quer fazer novamente? ')).upper().strip()[0]
print(' !FIM DO PROGRAMA! ')
