import os

os.system('cls')

#exemplo de vetor sem definição de tamanho usando a função split

entradaDados = input("[SYSTEM] Usuario, digite os elementos do vetor separados por espaço: ")
vetor = [int(x) for x in entradaDados.split()]

print(vetor)