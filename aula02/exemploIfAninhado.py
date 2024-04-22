import os

os.system('cls')

print(f"{'^_^' * 5} {'Programa Empréstimo'} {'^_^' * 5}")
print("Responda: \n1 - Sim.\n0 - Não.")

negativado = int(input("Possui nome negativado? "))

if negativado == 1:
    print("Voce não pode realizar empréstimos! :(")
else:

    carteiraAssinada = int(input("Possui carteira assinada? "))

    if carteiraAssinada == 0:
        print("Voce não pode realizar empréstimos! :(")
    else:

        casaPropria = int(input("Possui casa própria? "))

        if casaPropria == 0:
            print("Voce não pode realizar empréstimos! :(")
        else:
            print("Voce pode realizar empréstimos! :)")