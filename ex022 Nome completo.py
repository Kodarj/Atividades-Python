#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome

nome = str(input('Digite o seu nome completo: \n')).strip()
print('='*50)
print('Analisando seu nome...')
print('='*50)
print(f'Seu nome em maiusculo é: {nome.upper()} ')
print(f'Seu nome em minusculo é: {nome.lower()}')
nomes2 = nome.split()
nome = ''.join(nomes2)
print(f'A quantidade de letras no seu nome inteiro é: {len(nome)}') #print (f'Seu nome tem ao todo {len(nome) - nome.count(' ')}')
print(f'A quantidade de letras no seu primeiro nome é: {len(nomes2[0])}') #print (f'Seu primeiro nome tem {nome.find(' ')} letras')
