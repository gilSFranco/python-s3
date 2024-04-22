import os

os.system('cls')

linguagem = input("Usuário, me diga uma linguagem de programação: ")
listaLinguagens = ["python","c#","visual basic","c++","delphi","cobol","clipper","php","java"]
contador = 0

for i in listaLinguagens:
    if i == linguagem.lower():
        print(f"A linguagem {linguagem.capitalize()} foi encontrada na posição {contador}°.")
        break
    else:
        print(f"A linguagem não foi encontrada.")
    
    contador += 1
