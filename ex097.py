#Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.  
#lista
men = list()

#Função
def msg(text):
    for c in text:
        print('~'*(3+len(c)))
        print(f'  {c}')
        print('~'*(3+len(c)))


#Principal
while True:
    print()
    men.append(str(input('Digite sua mensagem: ')))
    print()
    while True:
        r = str(input('Quer adicionar mais uma mensagem? [S/N]: ')).upper().strip()[0]
        if r in 'SN':
            break
        print('Digite uma opção válida!')    
    if r == 'N':
        break

msg(men)