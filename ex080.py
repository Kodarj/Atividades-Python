# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista 
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

valores = list()
for c in range (0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > valores[-1]:
        valores.append(n)
        print('Valor inserido no final da lista')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Valor inserido na {pos}º posição.')
                break
            pos += 1
print('-='*40)
print(f'O valores digitados foram: {valores}')    
