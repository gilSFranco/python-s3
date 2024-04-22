import os

os.system('cls')

nome = input(f"Usuario, qual seu nome? ")
altura = float(input(f"{nome}, me diga sua altura: "))
sexo = input("Agora, qual seu sexo? (F ou M) ")

if sexo == "F":
    pesoIdeal = (62.1 * altura) - 44.7

    print(f"{nome}, seu peso ideal é {pesoIdeal:.2f}!")
elif sexo == "M":
    pesoIdeal = (72.7 * altura) - 58

    print(f"{nome}, seu peso ideal é {pesoIdeal:.2f}!")