salario = float(input("[SYSTEM] Usuario, qual o valor do seu salário? "))
reajuste = float(input("[SYSTEM] E o percentual de reajuste? "))

percentual = reajuste / 100
salarioPosReajuste = salario + (salario * percentual)

print(f"Seu salario era R${salario}, apos o reajuste de {reajuste}% é de R${salarioPosReajuste}!")