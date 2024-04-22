import os

os.system('cls')

matriz = []

for l in range(5):
    linha = []
    matriz.append(linha)

    for c in range(2):
        numeros = int(input(f"[SYSTEM] Usuario, digite um numero para a posição ({l},{c}): "))
        linha.append(numeros)

print("\n[SYSTEM] Usuario, sua matriz: ")
for m in matriz:
    print(m)