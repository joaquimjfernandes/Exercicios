# Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma sendo
# vendida respectivamente por 10, 12 e 15 reais. Construa um algoritmo em que o usuário forneça a
# quantidade de camisetas pequenas, médias e grandes referentes a uma venda, e a máquina
# informe quanto será o valor arrecadado

print('============= FrabriCaz Production ===============')

pequena = int(input('Quantas Camisetas Pequenas foram Vendidas: '))
media = int(input('Quantas Camisetas Médias foram Vendidas: '))
grande = int(input('Quantas Camisetas Grandes foram Vendidas: '))

totPagar = (pequena*10) + (media*12) + (grande*15)

# Mostando o Valor Total da Venda
print(f'O Total de todas Vendas deu o Valor de:{totPagar:.2f}R$')
