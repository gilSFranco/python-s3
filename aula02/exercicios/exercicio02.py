import os

os.system('cls')

nome1 = input("Usuario 1, me diga seu nome: ")
peso1 = float(input(f"{nome1}, qual seu peso? "))

nome2 = input("\nUsuario 2, me diga seu nome: ")
peso2 = float(input(f"{nome2}, qual seu peso? "))

if peso1 > peso2:
    print(f"\n{nome1}, você é mais pesado que o {nome2}(usuario 2)!")
elif peso2 > peso1:
    print(f"\n{nome2}, você é mais pesado que o {nome1}(usuario 1)!")
else:
    print(f"\n{nome1} e {nome2}, vocês possuem o mesmo peso!")