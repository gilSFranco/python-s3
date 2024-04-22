nome = input("[SYSTEM] Usuario, qual seu nome? ")
idade = int(input(f"[SYSTEM] {nome}, qual sua idade? "))

idadeEmDias = idade * 360

print(f"{nome} voce viveu {idadeEmDias} dias.")