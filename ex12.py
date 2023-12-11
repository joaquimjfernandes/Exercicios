# Peça para o usuário digitar o valor de um determinado produto. Se o produto
# custar acima de cem reais, o desconto concedido será de 20%. Caso contrário,
# somente 10% de desconto. Exiba o total a pagar com o desconto aplicado.
produto = str(input('Nome do Produto: '))
valor = int(input('Valor do Produto: '))

if valor > 1000:
    desc = valor - (valor * 20 / 100)
    print(f'O Total a Pagar com Desconto de 20% é {desc}')
else:
    desc = valor - (valor * 10 / 100)
    print(f'O Total a Pagar com Desconto de 10% é {desc}')
