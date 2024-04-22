nomes = ["José", "Maria Júlia", "Luiz", "Ana", "Fernanda"]

for i in nomes:
    if len(i) != 3:
        continue
    print(f"Olá, {i}!")

    if i == "Luiz":
        break