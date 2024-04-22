nome = input("[SYSTEM] Usuário, qual o produto que deseja comprar? ")
quantidade = int(input(f"[SYSTEM] E quantos {nome} deseja comprar? "))
preco = float(input("[SYSTEM] Por fim, qual o preço? "))

valorDaCompra = quantidade * preco

print(f"Usuário, você comprou {quantidade}(s) {nome}, e o valor total a pagar é {valorDaCompra}!")