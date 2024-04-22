import os

os.system('cls')

produto = input("Cliente, qual o nome do perfume? ")
preco = float(input(f"Qual o preço do {produto}? "))
quantidade = int(input("E a quantidade? "))

valorDaCompra = quantidade * preco

print(f"\n{'*' * 17} {'Loja de Perfumes'} {'*' * 17}")
print(f"{'*' * 7} {'                                    '} {'*' * 7}")
print(f"{'*' * 5} {'Código |  Forma de pagamento  | Desconto'} {'*' * 5}")
print(f"{'*' * 5} {'1      |  Á vista(em espécie) |       15'} {'*' * 5}")
print(f"{'*' * 5} {'2      |   Cartão de débito   |       10'} {'*' * 5}")
print(f"{'*' * 5} {'3      |  Cartão de crédito   |        5'} {'*' * 5}")
print(f"{'*' * 7} {'                                    '} {'*' * 7}")
print(f"{'*' * 17} {'Loja de Perfumes'} {'*' * 17}")

escolha = int(input("\nEscolha uma das formas de pagamento: (1, 2 ou 3) "))

match escolha:
    case 1:
        desconto = (valorDaCompra * 15) / 100
        valorFinal = valorDaCompra - desconto

        print(f"\nO valor da compra era de R${valorDaCompra:.2f}. Após 15% de desconto, é R${valorFinal:.2f}!\n")
    case 2:
        desconto = (valorDaCompra * 10) / 100
        valorFinal = valorDaCompra - desconto

        print(f"\nO valor da compra era de R${valorDaCompra:.2f}. Após 10% de desconto, é R${valorFinal:.2f}!\n")
    case 3:
        desconto = (valorDaCompra * 5) / 100
        valorFinal = valorDaCompra - desconto

        print(f"\nO valor da compra era de R${valorDaCompra:.2f}. Após 5% de desconto, é R${valorFinal:.2f}!\n")
    case _:
        print("\nDigite uma opção válida!\n")