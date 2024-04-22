import os

os.system('cls')

times = input("[SYSTEM] Usuario, digite o nome de times de futebol separados por espaço: ")
vetor = [str(x) for x in times.split()]

print("\n[SYSTEM] Usuario, voce digitou esses times:")
for i in vetor:
    print(i)