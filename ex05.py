"""Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste.
Calcular e escrever o valor do novo salário"""

# REAJUSTE SALÁRIAL DE UM FUNCIONÁRIO
salario = int(input('Salário Atual: '))

# Fazendo o Reajuste do Salário
salario_reajustado = salario+(salario*10/100)

print(f'O Novo Salário é de:{salario_reajustado}KZ')
