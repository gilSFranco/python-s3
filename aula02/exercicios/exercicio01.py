import os

os.system('cls')

numero1 = float(input("Usuario, digite o primeiro numero: "))
numero2 = float(input("Usuario, digite o segundo numero: "))

if numero1 > numero2:
    divisao = numero1 / numero2

    print(f"O numero {numero1} é maior que o numero {numero2}:\n{numero1} / {numero2} = {divisao}.")
elif numero2 > numero1:
    divisao = numero2 / numero1

    print(f"O numero {numero2} é maior que o numero {numero1}:\n{numero2} / {numero1} = {divisao}.")
else:
    print(f"Os numeros são iguais!")