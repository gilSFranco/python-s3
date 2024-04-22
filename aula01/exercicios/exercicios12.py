alturaParede = float(input("[SYSTEM] Usuário, qual é a altura dessa parede? "))
baseParede = float(input("[SYSTEM] E a base dela, quanto mede? "))

alturaAzulejo = float(input("\n[SYSTEM] Agora, qual é a altura do azulejo? "))
baseAzulejo = float(input("[SYSTEM] E quanto mede a base dele? "))

areaParede = alturaParede * baseParede
areaAzulejo = alturaAzulejo * baseAzulejo

quantidadeAzulejos = areaParede / areaAzulejo

print(f"\nNessa parede é possivel colocar {quantidadeAzulejos} azulejos!\n")