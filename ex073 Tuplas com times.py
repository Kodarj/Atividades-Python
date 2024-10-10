# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Cruzeiro.

time = ('Botafogo', 'Fortaleza', 'Palmeiras', 'Flamengo', 'Bahia', 'São Paulo', 'Cruzeiro', 'Atlético - MG', 'Athletico - PR', 'Vasco da Gama',
        'Juventude', 'Bragantino', 'Internacional', 'Criciuma', 'Gremio', 'EC Vitoria', 'Corithians', 'Fluminense', 'Cuiaba', 'Atlético - GO')
print('-='*40)
print(f'Lista dos times do brasileirão: {time}')
print('-='*40)
print(f'Os 5 primeiros colocados são: {time[0:5]}')
print('-='*40)
print(f'Os 4 últimos colocados são: {time[-4:]}')
print('-='*40)
print(f'Times em ordem alfabética: {sorted(time)}')
print('-='*40)
print(f'Posição do Cruzeiro é: {time.index('Cruzeiro')+1}º colocado.')
print('-='*40)