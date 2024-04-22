import os

os.system('cls')

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero: "))

if numero1 == numero2 and numero2 == numero3 and numero1 == numero3:
    print("Os numeros digitados são iguais.")
if numero1 > numero2 and numero1 > numero3:
    print(f"O {numero1} é o maior numero dentre os digitados!")
if numero2 > numero1 and numero2 > numero3:
    print(f"O {numero2} é o maior numero dentre os digitados!")
if numero3 > numero1 and numero3 > numero2:
    print(f"O {numero3} é o maior numero dentre os digitados!")