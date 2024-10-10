# Exercício Python 61 - 62: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

c = 9
t = 0
i = 0
print('GERADOR DE PA')
print('-=-'*25)
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a RAZÃO: '))
while c != 0:
    print(f' {n} ', end='')
    print(' -> ' if i < c else ' PAUSA!', end='')
    n += r
    if t == 9 :
        print()
        c = int(input('Quantos termos você quer mostrar a mais? '))
        i = 0
    elif i == c:
        print()
        c = int(input('Quantos termos você quer mostrar a mais? '))
        i = 0    
    t += 1
    i += 1
print(f'No total foram {t} termos mostrados.')
