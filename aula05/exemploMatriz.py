import os

os.system('cls')

linhas = int(input("[SYSTEM] Usuario, digite o numero de linhas da matriz: "))
colunas = int(input("[SYSTEM] Agora, digite o numero de colunas dela: "))

matrizNumeros = []

for l in range(linhas):
    linha = []
    matrizNumeros.append(linha)
    for c in range(colunas):
        numero = int(input(f"[SYSTEM] Digite o número para posição ({l}, {c}): "))

        linha.append(numero)

for m in matrizNumeros:
    print(m)