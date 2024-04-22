import os

os.system('cls')

numero1 = float(input("Usuario, digite o primeiro numero: "))
numero2 = float(input("Agora, digite o segundo numero: "))

# If

if numero1 < 0 or numero2 < 0:
    print("\nApenas numeros positivos são permitidos.")
    exit()

# If

print("\n1 - Média ponderada, com pesos 2 e 3, respectivamente.\n2 - Quadrado da soma dos 2 números.\n3 - Cubo do menor numero.")
escolhaDoUsuario = int(input("\nEscolha uma das opções acima: "))

if escolhaDoUsuario == 1:
    mediaPonderada = ((numero1 * 2) + (numero2 * 3)) / 5

    print(f"\nA média ponderada dos numeros {numero1} e {numero2}, é {mediaPonderada}!")

elif escolhaDoUsuario == 2:
    somaDosNumeros = numero1 + numero2
    quadrado = pow(somaDosNumeros, 2)

    print(f"\nO quadrado da soma dos numeros {numero1} e {numero2}, é {quadrado}!")

elif escolhaDoUsuario == 3:

    if numero1 < numero2:
        cubo = pow(numero1, 3)

        print(f"\nO cubo do numero {numero1}, é {cubo}!")
    else:
        cubo = pow(numero2, 3)

        print(f"\nO cubo do numero {numero2}, é {cubo}!")

else:
    print(f"\nOpção inválida!")
    exit()