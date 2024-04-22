import os

os.system('cls')

vogais = ["a","e","i","o","u"]
letras = []

for i in range(1,11):
    letra = input("Usuário, digite uma letra: ")
    letras.append(letra)

for vogal in vogais:
    for l in letras:
        if l == vogal:
            print(f"A letra {l} é uma vogal.")