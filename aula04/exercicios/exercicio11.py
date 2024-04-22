import os

os.system('cls')

nomes = ["luiz", "ana", "cristina", "fernanda", "maria alice", "joaquina"]
count = 1

while count != 0:
    if count == 1:
        print(f"\n{'*' * 5} {'Buscando nomes'} {'*' * 5}")
        print(f"{'*' * 1} {'1 - Começar a busca.'}   {'*' * 1}")
        print(f"{'*' * 1} {'0 - Finalizar a busca.'} {'*' * 1}")
        print(f"{'*' * 5} {'Buscando nomes'} {'*' * 5}\n")
    else:
        print(f"\n{'*' * 5} {'Buscando nomes'} {'*' * 5}")
        print(f"{'*' * 1} {'1 - Continuar a busca.'} {'*' * 1}")
        print(f"{'*' * 1} {'0 - Finalizar a busca.'} {'*' * 1}")
        print(f"{'*' * 5} {'Buscando nomes'} {'*' * 5}\n")

    escolha = int(input("Escolha uma das opções acima: (1 ou 0) "))

    if escolha == 1:
        busca = input("\nUsuario, me diga o nome que procura: ")
        
        for i in nomes:
            if i == busca.lower():
                print(f"O nome {i.capitalize()} pertence a lista.")
                break
            else:
                print(f"Nome não foi encontrado.")

    elif escolha == 0:
        break
    else: 
        print("Escolha uma opção válida.")

    count += 1