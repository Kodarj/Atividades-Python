from time import sleep
def lin():
    print('-='*40)


def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    #sleep(1.5)
    if i < f:
        lin()
        cont = p
        while cont <= f:
            print(f'{cont}', end=' ', flush = True)
            #sleep(0.5)
            cont += p
        print('FIM!')
    else:
        lin()
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush = True)
            cont -= p
            #sleep(0.5)
        print('FIM!')
        

contador(0,10,1)
contador(10,0,2)
lin()
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini,fim,passo)