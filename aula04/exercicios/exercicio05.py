import os

os.system('cls')

def bubbleSort(pontuacao):
    for p in range(len(pontuacao)-1, 0, -1):
        for i in range(p):
            if pontuacao[i] < pontuacao[i+1]:
                aux = pontuacao[i]
                pontuacao[i] = pontuacao[i+1]
                pontuacao[i+1] = aux

pontuacao = []
count = 1
soma = 0
contador = 0

while count < 5:
    print(f"\n{'*' * 5} {'Quiz - Sobre The Last Of Us(TLOU)'} {'*' * 5}")
    print("Quem matou joel?\n")
    print("A) - Abby.\nB) - Jesse.\nC) - Nora.\nD) - Marlene.")
    print(f"{'*' * 5} {'Quiz - Sobre nosso luizinho'} {'*' * 5}\n")

    escolha1 = input(f"Usuario {count}, escolha uma das opções: ")

    if escolha1 == "A":
        soma += 1

    print(f"\n{'*' * 5} {'Quiz - Sobre The Last Of Us(TLOU)'} {'*' * 5}")
    print("Por que a Ellie fez uma tatuagem em seu braço na parte II?\n")
    print("A) - Para irritar o joel, que não gosta de tatuagens.\nB) - Por puro estilo.\nC) - Para esconder a marca da mordida.\nD) - Por que ela se queimou.")
    print(f"{'*' * 5} {'Quiz - Sobre nosso luizinho'} {'*' * 5}\n")

    escolha2 = input(f"Usuario {count}, escolha uma das opções: ")

    if escolha2 == "C":
        soma += 1

    print(f"\n{'*' * 5} {'Quiz - Sobre The Last Of Us(TLOU)'} {'*' * 5}")
    print("Como se chamam os infectados que não enxergam?\n")
    print("A) - Espreitadores.\nB) - Baiacus.\nC) - Corredores.\nD) - Estaladores.")
    print(f"{'*' * 5} {'Quiz - Sobre nosso luizinho'} {'*' * 5}\n")

    escolha3 = input(f"Usuario {count}, escolha uma das opções: ")

    if escolha3 == "D":
        soma += 1

    pontuacao.append(soma)

    soma = 0

    count += 1

bubbleSort(pontuacao)

print("")
print(f"{'*' * 4} {'Ranking dos vencedores'} {'*' * 4}")
for i in pontuacao:
    contador += 1
    print(f"{contador}º lugar - Usuario {contador} ({i} pontos).")
print(f"{'*' * 4} {'Ranking dos vencedores'} {'*' * 4}")