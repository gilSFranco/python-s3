import os

os.system('cls')

print(f"{'*' * 11} {'Calculo de grandezas elétricas'} {'*' * 11}")
print("1 - Tensão(em Volt)            ----------     U = R * i\n2 - Resistência(em Ohm)        ----------     R = U / i\n3 - Corrente (em Ampére)       ----------     i = U / R.")
print(f"{'*' * 11} {'Calculo de grandezas elétricas'} {'*' * 11}")

escolha = int(input("\nEscolha uma das opções acima: "))

match escolha:
    case 1:
        resistencia = float(input("\nQual é o valor de 'R'? (em Ohm) "))
        corrente = float(input("E qual é o valor de 'i'? (em Ampére) "))

        tensao = resistencia * corrente

        print(f"\nA tensão vale {tensao:.2f} V!\n")
    case 2:
        tensao = float(input("\nQual é o valor de 'U'? (em Volt) "))
        corrente = float(input("E qual é o valor de 'i'? (em Ampére) "))

        resistencia = tensao / corrente

        print(f"\nA resistência vale {resistencia:.2f} Ohm!\n")
    case 3:
        tensao = float(input("\nQual é o valor de 'U'? (em Volt) "))
        resistencia = float(input("E qual é o valor de 'R'? (em Ohm) "))

        corrente = tensao / resistencia

        print(f"\nA corrente vale {corrente:.2f} Ampére!\n")
    case _:
        print("\nDigite uma opção válida!\n")