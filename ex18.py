# As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem
# compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e
# escreva o custo total da compra
macas = int(input('Quantas Maças queres Comprar: '))
if macas < 12:
    preco = macas * 1, 30
    print(f'O Total a Pagar pelas {macas}Maças é {preco}R$')
elif macas >= 12:
    preco = macas * 1, 00
    print(f'O Total a Pagar pelas {macas} é {preco}R$')
