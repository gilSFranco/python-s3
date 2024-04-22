import os

os.system('cls')

matriz = []

for l in range(2):
    linha = []
    matriz.append(linha)

    for c in range(3):
        capitais = input("[SYSTEM] Usuario, me diga o nome de uma capital do Brasil: ")
        linha.append(capitais)

print("\n[SYSTEM] Usuario, as capitais digitadas foram:")
for m in matriz:
    print(m)