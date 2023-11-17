# Tela Interativa
print('--'*15)
print('---      Tela Interativa    --')
print('--'*15)

sexo = str(input('Qual é o seu Genero[M/F]: ')).strip()

if sexo not in "Mm":
    print('Serás um Bom Programador Python!!!!')
elif sexo not in "Ff":
    print('Serás uma Boa Programadora JAVA')
else:
    print('Tenta Novamente')
