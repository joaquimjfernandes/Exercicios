# Faça um programa em que o usuário digite a sigla de um estado (ex.: RJ, SP). Se
# este estado for SP, escreva Paulista, se RJ, escreva Carioca, se MG, escreva Mineiro.
# Caso seja outro estado, escreva Outro Estado
estado = str(input('Qual é o teu Estado: ')).upper()
if estado == 'SP':
    print('Você é Paulista')
elif estado == 'RJ':
    print('Você é Carioca')
elif estado == 'MG':
    print('Você é Mineiro')
else:
    print('Você é de Outro Estado')
