votosBrancos = int(input("[SYSTEM] Qual o numero de votos brancos? "))
votosNulos = int(input("[SYSTEM] Qual o numero de votos nulos? "))
votosValidos = int(input("[SYSTEM] E qual o numero de votos validos? "))

totalEleitores = votosBrancos + votosNulos + votosValidos

percentualBrancos = (votosBrancos * 100) / totalEleitores
percentualNulos = (votosNulos * 100) / totalEleitores
percentualValidos = (votosValidos * 100) / totalEleitores

print(f"\nNos tivemos {totalEleitores} eleitores e os votos deles foram: \
      \n\nVotos brancos - {percentualBrancos}%. \
      \nVotos nulos - {percentualNulos}%. \
      \nVotos validos - {percentualValidos}%.\n")