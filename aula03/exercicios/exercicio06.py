import os

os.system('cls')

pesoPessoa = float(input("Usuario, me diga seu peso: "))

print(f"\n{'*' * 12} {'Gravidade dos Planetas'} {'*' * 12}")
print(f"{'*' * 7} {'                                '} {'*' * 7}")
print(f"{'*' * 5} {'Numero    |  Gravidade  |    Planeta'} {'*' * 5}")
print(f"{'*' * 5} {'1         |    0,37     |   Mercúrio'} {'*' * 5}")
print(f"{'*' * 5} {'2         |    0,88     |      Vênus'} {'*' * 5}")
print(f"{'*' * 5} {'3         |    0,38     |      Marte'} {'*' * 5}")
print(f"{'*' * 5} {'4         |    2,64     |    Júpiter'} {'*' * 5}")
print(f"{'*' * 5} {'5         |    1,15     |    Saturno'} {'*' * 5}")
print(f"{'*' * 7} {'                                '} {'*' * 7}")
print(f"{'*' * 12} {'Gravidade dos Planetas'} {'*' * 12}")

gravidade = int(input("\nAgora, me informe o planeta escolhido por você: "))

match gravidade:
    case 1:
        peso = pesoPessoa * 0.37

        print(f"\nNa terra você pesa {pesoPessoa:.2f}Kg. Em Mercúrio o seu peso seria {peso:.2f}Kg!\n")
    case 2:
        peso = pesoPessoa * 0.88

        print(f"\nNa terra você pesa {pesoPessoa:.2f}Kg. Em Vênus o seu peso seria {peso:.2f}Kg!\n")
    case 3:
        peso = pesoPessoa * 0.38

        print(f"\nNa terra você pesa {pesoPessoa:.2f}Kg. Em Marte o seu peso seria {peso:.2f}Kg!\n")
    case 4:
        peso = pesoPessoa * 2.64

        print(f"\nNa terra você pesa {pesoPessoa:.2f}Kg. Em Júpiter o seu peso seria {peso:.2f}Kg!\n")
    case 5:
        peso = pesoPessoa * 1.15

        print(f"\nNa terra você pesa {pesoPessoa:.2f}Kg. Em Saturno o seu peso seria {peso:.2f}Kg!\n")