import os

os.system('cls')

linguagens = ["python","c#","Visual Basic","C++","Delphi","Cobol"]
soma = 0

print(f"As linguagens com mais de 3 caracteres na lista são:\n")
for i in linguagens:
    soma = soma + len(i)
    if len(i) > 3:
        print(i)

print(f"\nA soma de todos os caracteres desta lista de linguagens é de: {soma}!")