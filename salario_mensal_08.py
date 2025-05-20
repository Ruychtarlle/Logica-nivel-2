# 8) Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste. Calcular e escrever o valor do novo salário

salario_atual = float(input("Digite o salário atual: "))
percentual_reajuste = float(input("Digite o percentual de reajuste: "))

salario_Novo = salario_atual * (1 + percentual_reajuste/100)

print("O novo salário é: ", salario_Novo)
