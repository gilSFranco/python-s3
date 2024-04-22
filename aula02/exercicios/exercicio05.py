import os

os.system('cls')

nome1 = input(f"\nUsuario 1, qual seu nome? ")
altura1 = float(input(f"{nome1}, me diga sua altura: "))

nome2 = input(f"\nUsuario 2, qual seu nome? ")
altura2 = float(input(f"{nome2}, me diga sua altura: "))

nome3 = input(f"\nUsuario 3, qual seu nome? ")
altura3 = float(input(f"{nome3}, me diga sua altura: "))

if altura1 > altura2 and altura1 > altura3:
    
    if altura2 > altura3:
        print(f"\nAs estaturas em ordem decrescente são:\n- {nome1}({altura1}).\n- {nome2}({altura2}).\n- {nome3}({altura3}).")
    else:
        print(f"\nAs estaturas em ordem decrescente são:\n- {nome1}({altura1}).\n- {nome3}({altura3}).\n- {nome2}({altura2}).")

elif altura2 > altura1 and altura2 > altura3:

    if altura1 > altura3:
        print(f"\nAs estaturas em ordem decrescente são:\n- {nome2}({altura2}).\n- {nome1}({altura1}).\n- {nome3}({altura3}).")
    else:
        print(f"\nAs estaturas em ordem decrescente são:\n- {nome2}({altura2}).\n- {nome3}({altura3}).\n- {nome1}({altura1}).")

elif altura3 > altura1 and altura3 > altura2:

    if altura1 > altura2:
        print(f"\nAs estaturas em ordem decrescente são:\n- {nome3}({altura3}).\n- {nome1}({altura1}).\n- {nome2}({altura2}).")
    else:
        print(f"\nAs estaturas em ordem decrescente são:\n- {nome3}({altura3}).\n- {nome2}({altura2}).\n- {nome1}({altura1}).")

else:
    print(f"Algo deu errado.")