# Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três, impares e que se encontram no intervalo de 1 até 500.
s = 0
c = 0
for n in range(1,501, 2):
        if n % 3 == 0:
            c = c + 1
            s = s + n
print(f'A soma de todos os {c} valores solicitados é {s} ')