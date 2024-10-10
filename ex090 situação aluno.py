# Exercício Python 090: Faça um programa que leia nome e média de um aluno, 
# guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela

aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média do {aluno['nome']}: '))
print('-='*40)
print(f'- O aluno {aluno['nome']} está com uma média de {aluno['media']} e sua situação é: ')

if aluno['media'] >= 7:
    aluno['situacao'] = 'APROVADO!'
elif 5<= aluno['media'] < 7:
    aluno['situacao'] = 'RECUPERAÇÃO!'
else:
    aluno['situacao'] = 'REPROVADO!'

print(f'--------- {aluno['situacao']} ---------')