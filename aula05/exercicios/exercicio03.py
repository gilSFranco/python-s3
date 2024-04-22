import os

os.system('cls')

numeros = input("[SYSTEM] Usuario, digite numeros separados por espaço: ")
vetor = [int(x) for x in numeros.split()]
par = []

print("\n[SYSTEM] Usuario, os numeros que voce digitou foram:")
for i in vetor:
    print(i)
    if i % 2 == 0:
        par.append(i)

print("\nDentre os digitados, esses são pares:")
for p in par:
    print(p)