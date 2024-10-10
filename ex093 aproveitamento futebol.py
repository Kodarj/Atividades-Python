# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

registro = dict()
gols = list()

registro['nome'] = str(input('Nome do jogador: '))
par = int(input(f'Quantas partidas o jogador {registro['nome']} jogou? '))

for c in range (1,par+1):
    gols.append(int(input(f'Gols na partida {c}: ')))

registro['gol'] = gols[:] # colocar lista dentro de dicionario
registro['total'] = sum(gols) # fazendo isso, vai somar todos os valores da lista e colocar no dicionário o total.

print('-='*40)
print(registro)
print('-='*40)

for k,v in registro.items():
    print(f' O campo {k} tem o valor {v}')

print('-='*40)

print(f'O jogador {registro['nome']} jogou {len(registro["gol"])} partidas.')
print()

for c, p in enumerate(registro['gol']):
    print(f' => Na partida {c+1}, fez {p} gols')

print()    
print(f'Foi um total de {registro['total']} gols.')
print('-='*40)

