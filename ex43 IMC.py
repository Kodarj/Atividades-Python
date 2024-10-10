# Cabeçalho
print("="*45)
print("         TABELA DE IMC               ")
print("="*45)
r = True
#entrada de dados:
while (r == True):
    nome = input("DIGITE SEU NOME:\n")
    idade = int(input("DIGITE SUA IDADE:\n"))
    peso = float(input("DIGITE SEU PESO:\n"))
    altura = float(input("DIGITE SUA ALTURA:\n"))

    #processamento e saida de dados
    imc = (peso/(altura*altura))

    if (imc>30):
        print(f"{nome}, seu imc é {imc:.1f}, e você está no grau de obesidade")
    elif ((imc<30)and(imc>25)):
        print(f"{nome}, seu imc é {imc:.1f}, e você está no grau de sobrepeso")

    elif ((imc<25)and(imc>18)):
        print(f"{nome}, seu imc é {imc:.1f}, e você está no grau peso normal")

    else:
        print(f"{nome}, seu imc é {imc:.1f}, e você está no grau de baixo peso")
    #finalização
    resp = input("Gostaria de recomeçar?\n")
    if ((resp == "não") or (resp == "Não") or (resp == "nao") or (resp == "n")):
        r = False

print("="*45)
print("FIM DO PROGRAMA")
print("="*45)