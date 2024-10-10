prod = float(input('Digite o valor do produto: '))
desc = float(input('Digite o valor do Desconto que vai ser aplicado: '))

print(f'O valor do produto com o desconto irá ser: R${prod-(prod*(desc/100)):.2f}')
