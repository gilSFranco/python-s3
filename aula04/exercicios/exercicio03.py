import os

os.system('cls')

numero = int(input("Usuario, digite o numero o qual voce quer ver a tabuada: "))
count = 1

print(f"\nTabuada de: {numero}.")

while count <= 10:
    print(f"{numero} x {count} = {numero * count}.")
    count += 1