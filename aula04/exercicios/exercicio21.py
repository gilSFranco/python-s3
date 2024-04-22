import os

os.system('cls')

class Funcionario:
    def __init__(self, nome, sexo):
        self.nome = nome
        self.sexo = sexo

funcionarios = []
count = 1

while count <= 2:
    nome = input("\nFuncionário, qual seu nome? ")
    sexo = input("E o seu sexo? (F ou M) ")

    if sexo != "F" and sexo != "M":
        print("Funcionario, digite o sexo corretamente.")
        break

    funcionario = Funcionario(nome, sexo)
    funcionarios.append(funcionario)
    
    count += 1

print("")

for i in funcionarios:
    if i.sexo == "M":
        print(f"O funcionário {i.nome} precisa fazer o exame.")