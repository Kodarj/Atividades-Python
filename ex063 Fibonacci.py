# entrada de dados:
qnt = int(input("Digite a quantidade de valor que você quer saber da sequencia de fibonacci:\n"))
i = 0
n1 = 0
n2 = 0
n3 = 0
# processamento e saida
while (i<=qnt):
    print(n2 , end=' ')
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    if (n2<1):
        n2 = 1
    i = i + 1
print()
print("FIM DO PROGRAMA")

