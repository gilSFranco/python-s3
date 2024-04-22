import os

os.system('cls')

numerosPares = []
numerosImpares = []

for i in range(1,11):
    numero = int(input("Usuário, digite um número inteiro: "))

    if numero % 2 == 0:
        numerosPares.append(numero)
    else:
        numerosImpares.append(numero)

print("\nOs números pares são:\n")
for i in numerosPares:
    print(f"{i}.")

print("\nE os números impares:\n")
for i in numerosImpares:
    print(f"{i}.")