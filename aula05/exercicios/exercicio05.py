import os

os.system('cls')

matriz = []
maiores = []
contador = 0

for l in range(4):
    linha = []
    matriz.append(linha)

    for c in range(4):
        numeros = int(input(f"[SYSTEM] Usuario, digite um numero para a posição ({l},{c}): "))
        linha.append(numeros)

        if numeros > 10:
            maiores.append(numeros)
            contador+=1

print("\n[SYSTEM] Usuario, os numeros maiores que 10 dessa matriz são:")
for m in maiores:
    print(m)
print(f"\nContando, temos {contador}.")