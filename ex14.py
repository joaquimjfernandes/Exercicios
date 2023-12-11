# Digite o sexo (M ou F) de cinco pessoas. Informe quantos homens e quantas
# mulheres foram preenchidos.
f = 0
m = 0
for s in range(1, 6):
    sexo = str(input('Qual é o seu Genero(F/M): '))
    if sexo in 'Ff':
        f += 1
    elif sexo in 'Mm':
        m += 1
print(f'Foram digitadas {f} Mulheres ==> E Foram digitados {m} Homens')
