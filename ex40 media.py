n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2)/2

if media < 5:
    print(f'Média de : {media:.1f} . REPROVADO!')
elif 7> media >= 5:
    print(f'Média de : {media:.1f} . RECUPERAÇÃO!')
else:
    print(f'Média de : {media:.1f} . APROVADO!')
