# Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.
print('*============* MAIOR NÚMERO *============*')
v1 = int(input('Digite um Valor: '))
v2 = int(input('Digite um Valor: '))
v3 = int(input('Digite um Valor: '))
if v1 > v2 and v1 > v3:
    print(f'{v1} é MAIOR entre todos os Valores Digitados')
elif v2 > v1 and v2 > v3:
    print(f'{v2} é MAIOR entre todos os Valores Digitados')
elif v3 > v1 and v3 > v2:
    print(f'{v3} é MAIOR entre todos os Valores Digitados')

# ------------------//--------------------
if v1 == v2:
    print(f'{v1} e {v2} são Iguais!')
elif v2 == v3:
    print(f'{v2} e {v3} são Iguais!')
elif v3 == v1:
    print(f'{v1} e {v2} são Iguais!')

# ------------------//--------------------
if v1 == v2 and v1 == v3:
    print('Todos os Valores Acima Digitados são Iguais')
