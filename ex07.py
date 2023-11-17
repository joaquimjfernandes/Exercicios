# IMC -> Índice de Massa Corporal

print('IMC Calculator')
print('-'*25)

# Recebendo todos os Dados
sexo = str(input('Insira o seu Genero[M/F]: '))
altura = float(input('Insira a sua Altura[cm]: '))

# Verificando e fazendo as condições
if sexo in "Mm":
    peso = (72.2 * altura) - 58
    print(f'O seu Peso ideal é de {peso}')
elif sexo in "Ff":
    peso = (62.1 * altura) - 44.7
    print(f'O seu Peso ideal é de {peso}')
