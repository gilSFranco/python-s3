import os
os.system('cls')

nome = input("Usuario, me diga seu nome: ")
nota1 = float(input(f"{nome}, digite a primeira nota: "))
nota2 = float(input(f"{nome}, digite a segunda nota: "))

media = (nota1 + nota2)/2

if media > 6:
    print(f"{nome}, você está aprovado! Sua média é de {media:.2f}.")
elif media >= 2 and media <= 6:
    print(f"{nome}, você está de exame!")
else:
    print(f"{nome}, você está reprovado! Sua média foi de {media:.2f}, e está abaixo do esperado.")