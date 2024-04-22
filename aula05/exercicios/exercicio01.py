import os

os.system('cls')

vetor = []

for i in range(5):
    cor = input("[SYSTEM] Usuario, digite uma cor: ")
    vetor.append(cor)

print("\n[SYSTEM] Usuario, voce digitou as cores:")
for i in vetor:
    print(i)