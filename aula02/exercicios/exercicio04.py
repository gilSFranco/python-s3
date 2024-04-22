import os

os.system('cls')

numero = int(input("Usuario, digite um numero: "))

if numero > 0:
    resto = numero % 2

    if resto == 0:
        quadrado = pow(numero, 2)

        print(f"O numero {numero} é par:\n{numero}² = {quadrado}!")
    else:
        cubo = pow(numero, 3)

        print(f"O numero {numero} é impar:\n{numero}³ = {cubo}!")