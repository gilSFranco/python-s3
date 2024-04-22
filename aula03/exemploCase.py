op = int(input("1- Sacar \n 2- Extrato \n 3- Sair \n Escolha a opção: "))
 
match op:
    case 1:
        print("Sacar")
        valor = float(input("Digite o valor a sacar: R$"))
        print(f"Valor Retirado: {valor}")
    case 2:
        print("Extrato")
        dias = int(input("Digite a quantidade de dias do extrato: "))
        print(f"Retirando o extrato de {dias} dias")
    case 3:
        print("Sair")
        exit()
    case _ :
        print("Opção Inválida")
 
# match op.upper(): |  Utilize essa opção para transformar a letra em maiusculas
#    case "A":      |
 
# match op.lower(): |  Utilize essa opção para transformar a letra em maiusculas
#    case "A":      |
 
# Para usar com caracteres
# match op:
#   case "A" | "a":
#   Para transformar em letras maiusculas variavel.upper()
#   Para transformar em letras minusculas variavel.lower()