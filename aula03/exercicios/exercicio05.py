import os

os.system('cls')

salario = float(input("Funcionario, qual o valor do seu salário? "))
categoria = input("E qual a sua categoria? (A, B ou C) ")

match categoria:
    case 'A':
        desconto = (salario * 10) / 100
        valorFinal = salario + desconto

        print(f"\nO seu salário era de R${salario:.2f}. Após 10% de aumento, é R${valorFinal:.2f}!\n")
    case 'B':
        desconto = (salario * 15) / 100
        valorFinal = salario + desconto

        print(f"\nO seu salário era de R${salario:.2f}. Após 15% de aumento, é R${valorFinal:.2f}!\n")
    case 'C':
        desconto = (salario * 25) / 100
        valorFinal = salario + desconto

        print(f"\nO seu salário era de R${salario:.2f}. Após 25% de aumento, é R${valorFinal:.2f}!\n")
    case _:
        print("\nDigite uma opção válida!\n")