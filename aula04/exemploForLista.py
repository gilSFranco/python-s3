import os

os.system('cls')

frutas = ["Morango", "Abacate", "Banana"]

for lista in frutas:
    print(lista)

#Buscar nome da fruta - Sem input do usuario
busca = "Banana"
frutas = ["Morango", "Abacate", "Banana"]

for i in frutas:
    if i == busca:
        print("Fruta encontrada.")
        break
    else:
        print(f"{busca}, não foi encontrada.")

#Buscar nome da fruta - Com input do usuario
busca = input("Usuario, me diga a fruta que procura: ")
frutas = ["morango", "abacate", "banana"]

for i in frutas:
    if i == busca.lower():
        print("Fruta encontrada.")
        break
    else:
        print(f"{busca}, não foi encontrada.")