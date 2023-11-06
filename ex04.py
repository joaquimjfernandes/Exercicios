# CÁLCULO DE ELEITORES
"""Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos
em branco, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total
de eleitores."""

# Recebendo todos os DADOS
eleitores = int(input('Total de Eleitores (Município): '))
votos_brancos = int(input('Total de Votos em Branco: '))
votos_nulos = int(input('Total de Votos Nulos: '))
votos_validos = int(input('Total de Votos Válidos: '))
print('-'*35)
# Cálculo Percentual dos Votos em Brancos
tot_branco = (votos_brancos / eleitores) * 100

# Cálculo Percentual Votos em Nulos
tot_nulo = (votos_nulos / eleitores) * 100

# Cálculo Percentual Votos Válidos
tot_valido = (votos_validos / eleitores) * 100

# Mostrando na Tela o Total de todos Votos!!
print(f'Total de Votos em Brancos: {tot_branco:.2f}%')
print(f'Total de Votos em Brancos: {tot_nulo:.2f}%')
print(f'Total de Votos em Brancos: {tot_valido:.2f}%')
