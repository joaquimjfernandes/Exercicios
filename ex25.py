# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# até 20 litros, desconto de 3% por litro Álcool
# acima de 20 litros, desconto de 5% por litro
# até 20 litros, desconto de 4% por litro Gasolina
# acima de 20 litros, desconto de 6% por litro

# Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível (codificado da
# seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se
# que o preço do litro da gasolina é R$ 300 e o preço do litro do álcool é R$ 200.

a = int(input('Quantos Litros de Álcool: '))
g = int(input('Quantos Litros de Gasolina: '))
desc_a = (a * 200) + (a*3/100)
desc_g = (g*300) + (g*4/100)
