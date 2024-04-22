import os

os.system('cls')

indiceDePoluicao = int(input("Qual é o índice de poluição atual? "))

match indiceDePoluicao:
    case 0 | 1 | 2:
        print(f"\nO índice de poluição é de {indiceDePoluicao}!\n{indiceDePoluicao} é considerado aceitável.\n")
    case 3 | 4 | 5:
        print(f"\nO índice de poluição é de {indiceDePoluicao}!\nCom {indiceDePoluicao} é recomendado suspender as atividades do grupo I.\n")
    case 6 | 7:
        print(f"\nO índice de poluição é de {indiceDePoluicao}!\nCom {indiceDePoluicao} é recomendado suspender as atividades do grupo I e do II.\n")
    case indiceDePoluicao if indiceDePoluicao >= 8:
        print(f"\nO índice de poluição é de {indiceDePoluicao}!\nCom {indiceDePoluicao} é recomendado suspender as atividades de todos os grupos.\n")