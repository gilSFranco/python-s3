import os

os.system('cls')

precos = []
countw = 1

while countw != 0:
      if countw == 1:
            print(f"\n{'*' * 6} {'Lojas do luiz'} {'*' * 6}")
            print(f"{'*' * 1} {'1 - Começar a compra.'}   {'*' * 1}")
            print(f"{'*' * 1} {'2 - Finalizar a compra.'} {'*' * 1}")
            print(f"{'*' * 6} {'Lojas do Luiz'} {'*' * 6}\n")
      else:
            print(f"\n{'*' * 6} {'Lojas do luiz'} {'*' * 6}")
            print(f"{'*' * 1} {'1 - Continuar a compra.'} {'*' * 1}")
            print(f"{'*' * 1} {'2 - Finalizar a compra.'} {'*' * 1}")
            print(f"{'*' * 6} {'Lojas do Luiz'} {'*' * 6}\n")

      escolha = int(input("Escolha uma das opções acima: (1 ou 2) "))

      if escolha == 1:
            preco = float(input(f"\nQual o preço do produto {countw}? "))
            precos.append(preco)

      elif escolha == 2:
            break

      else: 
            print("Escolha uma opção válida.")

      countw += 1

countf = 0
soma = 0

pagamento = float(input("\nCliente, quanto dinheiro você possui em sua posse? "))

print(f"\n{'*' * 7} {'Lojas do luiz'} {'*' * 6}")
for i in precos:
      soma = soma + i
      countf += 1
      print(f"{'*' * 3}    Produto {countf}: {i}.  {'*' * 3}")

print(f"{'*' * 28}")
print(f"{'*' * 3} Total a pagar: {soma}. {'*' * 3}")
print(f"{'*' * 3}   Pagamento: {pagamento}.   {'*' * 3}")
print(f"{'*' * 3}      Troco: {pagamento - soma}.     {'*' * 3}")
print(f"{'*' * 7} {'Lojas do luiz'} {'*' * 6}\n")