import os

os.system('cls')

quantidadeDinheiro = float(input("Usuário, os preços começarão a ser mostrados a partir de quantos R$? "))

print(f"\n{'*' * 5} {'Panificadora Pão de Ontem'} {'*' * 5}")
for i in range(2,51,2):
      preco = i * 0.18

      if preco >= quantidadeDinheiro:
            print(f"{i}° - R${preco:.2f}")
print(f"{'*' * 5} {'Panificadora Pão de Ontem'} {'*' * 5}")