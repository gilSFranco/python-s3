import os
from datetime import date

os.system('cls')

rg = input("Funcionario, qual seu rg? ")
anoNascimento = int(input("Agora, me diga seu ano de nascimento: "))
anoIngresso = int(input("E qual o ano em que voce ingressou na empresa? "))
anoAtual = date.today().year

idade = anoAtual - anoNascimento
tempoTrabalho = anoAtual - anoIngresso

print(f"{idade} e {tempoTrabalho}")

if idade >= 65 or tempoTrabalho >= 30:
    print("Requerer aposentadoria!")
elif idade >= 60 and tempoTrabalho >= 25:
    print("Requerer aposentadoria! :(")
else:
    print("Não requerer aposentadoria.")