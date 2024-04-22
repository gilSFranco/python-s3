import os

os.system('cls')

numero = int(input("Usuario, digite o numero o qual voce quer ver a tabuada: "))
inicial = int(input("Agora, a tabuada começará por qual numero: "))
final = int(input("E terminará em qual numero: "))

print(f"\nTabuada de: {numero}.")

while inicial <= final:
    print(f"{numero} x {inicial} = {numero * inicial}.")
    inicial += 1