# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:  
# A) A soma de todos os valores pares digitados.                                                                                               
# B) A soma dos valores da terceira coluna.             
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
maior = 0
par = 0
soma = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor de [{l}, {c}]: '))

print('-='*40)

for l in range (0,3):
    for c in range(0,3):
        if matriz[l][c] % 2 == 0:
            par = par + matriz[l][c]
        if c == 2:
            soma = soma + matriz[l][c]
        if l == 1:
            if c == 0:
                maior = matriz[l][c]
            else:
                if maior < matriz[l][c]:
                    maior = matriz[l][c]
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('-='*40)
print(f'A soma dos valores pares é de : {par}')
print(f'A soma dos valores da terceira coluna é: {soma}')
print(f'O maior valor da segunda linha é: {maior}')
        
        