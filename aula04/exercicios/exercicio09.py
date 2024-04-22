import os

os.system('cls')

busca = input("Usuario, me diga o nome que procura: ")
nomes = ["maria", "joao", "paulo", "magali"]

for i in nomes:
    if i == busca.lower():
        print(f"O nome {i.capitalize()} pertence a lista.")
        break
    else:
        print(f"Nome não foi encontrado.")