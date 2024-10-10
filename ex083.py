# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
par = 0
paren = 0

form = str(input('Digite a expressão: '))

for c in form:
    if c == '(':
        par +=1
    elif c == ')':
        paren +=1
        
if par == paren:
    print('Sua expressão é válida.')
else:
    print('Sua expressão não é válida.')
