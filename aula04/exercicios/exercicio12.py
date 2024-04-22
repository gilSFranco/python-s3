import os

os.system('cls')

listaNomes = []
contador = 0

for i in range(1,8):
    nome = input("Usuário, digite um nome: ")
    listaNomes.append(nome)

for i in listaNomes:
    contador += 1
    print(f"O {contador}° nome armazenado é {i}.")