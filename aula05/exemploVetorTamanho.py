import os

os.system('cls')

#exemplo de vetor com definição de tamanho
tamanho = int(input("[SYSTEM] Usuario, digite o tamanho do vetor: "))

vetor = []

for i in range(tamanho):
    elemento = int(input(f"[SYSTEM] Agora, digite o {i + 1}º valor do vetor: "))
    vetor.append(elemento)

print(vetor)