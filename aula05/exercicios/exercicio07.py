import os

os.system('cls')

matriz = []

for l in range(5):
    linha = []
    matriz.append(linha)

    for c in range(2):
        if c == 1:
            quantidades = int(input("[SYSTEM] Agora usuario, me diga agora a quantidade desse produto: "))
            linha.append(quantidades)
            print("")
        else:
            nomes = input("[SYSTEM] Usuario, qual o nome do produto? ")
            linha.append(nomes)

print("\n[SYSTEM] Usuario, os produtos cadastrados foram:")
for m in matriz:
    print(m)