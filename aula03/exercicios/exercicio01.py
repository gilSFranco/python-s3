import os

os.system('cls')

letra = input("Usuario, digite uma letra qualquer: ")

match letra:
    case 'a':
        print(f"A letra {letra} é uma vogal!")
    case 'e':
        print(f"A letra {letra} é uma vogal!")
    case 'i':
        print(f"A letra {letra} é uma vogal!")
    case 'o':
        print(f"A letra {letra} é uma vogal!")
    case 'u':
        print(f"A letra {letra} é uma vogal!")
    case _:
        print(f"A letra {letra} é uma consoante!")