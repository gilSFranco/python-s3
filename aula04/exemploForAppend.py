import os

os.system('cls')

numeros = []

for i in range(1,6):
    numero = int(input(f"Usuario, digite o {i}º numero: "))
    numeros.append(numero)

for i in numeros:
    print(i)