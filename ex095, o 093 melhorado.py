# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

cad = list()
registro = dict()
gols = list()

while True:
    registro.clear()
   
    print('-='*40)
    registro['nome'] = str(input('Nome do jogador: '))
    par = int(input(f'Quantas partidas o jogador {registro['nome']} jogou? '))

    for c in range (1,par+1):
        gols.append(int(input(f'    Gols na partida {c}: ')))

    registro['gol'] = gols[:] # colocar lista dentro de dicionario
    registro['total'] = sum(gols) # fazendo isso, vai somar todos os valores da lista e colocar no dicionário o total.
    gols.clear()
    cad.append(registro.copy())
    while True:
        resp = str(input('Quer Continuar? ')).upper().strip()[0]
        if resp in 'SN':
            break    
        print('ERRO! DIGITE UMA OPÇÃO VÁLIDA!')         
    if resp == 'N':
        break

print('-='*40)
print('COD ',end='')
for i in registro.keys():
    print(f'{i:<15} ',end='') # fazer a cabeçalho
print()
print('-'*40)

for c,v in enumerate(cad):
    print(f'{c:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ') # organizar a tabela
    print()

while True:
    print('-'*40)
    r = int(input('Mostrar dado de qual jogador [999 para encerrar]:  '))
    if r == 999:
        break
    if r >= len(cad):
        print(f'ERRO! Não existe jogador com código {r}') 
    else:
        print(f'-- Levantamento do jogador: {cad[r]["nome"]}')
        for p,x in enumerate(cad[r]['gol']):
            print(f'        No jogo {p+1} fez {x} gols')    


print('>>>>> FIM DO PROGRAMA <<<<<')


print('-'*40)