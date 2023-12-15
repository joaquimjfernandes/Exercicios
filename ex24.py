# Ler dois valores e imprimir uma das três mensagens a seguir:
# ‘Números iguais’, caso os números sejam iguais
# ‘Primeiro é maior’, caso o primeiro seja maior que o segundo;
# ‘Segundo maior’, caso o segundo seja maior que o primeiro.
def numverify():
    if n1 == n2:
        print('Os Dois Números são Iguais!')
    elif n1 > n2:
        print('O Primeiro Número é MAIOR')
    elif n2 > n1:
        print('O Segundo Número é MAIOR')


n1 = int(input('Insira um Valor: '))
n2 = int(input('Insira um Valor: '))

numverify()
