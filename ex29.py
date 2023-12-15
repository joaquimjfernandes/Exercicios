# Escreva um algoritmo para ler 2 valores e se o segundo valor informado for ZERO, deve ser lido
# um novo valor, ou seja, para o segundo valor não pode ser aceite o valor zero e imprimir o resultado
# da divisão do primeiro valor lido pelo segundo valor lido.
# Acrescentar uma mensagem de 'VALOR INVÁLIDO' no exercício [45] caso o segundo valor
# informado seja ZERO.

v1 = int(input('Digite um Valor: '))
v2 = int(input('Digite um Valor: '))
print('-'*35)
# Validação dos Dados
if v2 == 0:
    print('-'*30)
    print('VALOR INVÁLIDO')
    v2 = int(input('Digite Outro Número Diferente de Zero[0]: '))
divisao = v1 / v2
print(f'A Divisão entre os Valores é => {divisao}')
