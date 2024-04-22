from math import pi

raio = float(input("[SYSTEM] Usuario, qual é o valor do raio desse cilindro? "))
altura = float(input("[SYSTEM] E qual é a altura dele? "))

volume = pi * (pow(raio, 2)) * altura

print(f"O volume do cilindro é de {volume:.2f}!")