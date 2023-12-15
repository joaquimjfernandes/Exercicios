# Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores.
v1 = int(input('Insira um Valor: '))
v2 = int(input('Insira um Valor: '))
v3 = int(input('Insira um Valor: '))
soma = 0
if v1 > v2 and v1 > v3:
    print(v1)
elif v2 > v3 and v2 > v1:
    print(v2)
elif v3 > v1 and v3 > v2:
    print(v3)
