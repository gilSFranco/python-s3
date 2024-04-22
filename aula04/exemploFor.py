import os

os.system('cls')

#Repeticao for de 1 até 100
for i in range(1,101):
    print(i)

soma = 0

#Repeticao for de 1 até 100 - Somando todos os numeros
for i in range(1,101):
    soma += i

print(f"A soma total de 1 a 100 é: {soma}")

#Repeticao for de 1 até 100 - Pulando de 2 em 2
for i in range(1,101,2):
    print(i)