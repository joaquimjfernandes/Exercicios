def adicao():
    soma = n1 + n2

def subtra():
    subtr = n1 - n2

def divi():
    div = n1 / n2

def multi():
    mu = n1 * n2

def maiorI():
    mair = n1 > n2
    Igual = n1 == n2


while True:
    print('''[1] Adição
    [2] Subtração
    [3] Divisão
    [4] Multiplicação
    [5] Mairidade e Igualdade
    [6] Sair do Programa''')
    op = int(input('Oque Desejas Fazer: '))

    if op == 1:
        n1 = int(input('Digite um Número: '))
        n2 = int(input('Digite um Número: '))
        adicao()
        other = str(input('Desejas Continuar[S/N]: '))
        while other not in 'Ss':
            other = str(input('Opção Inválida, \n '))
            if other in 'Nn':
                break

    elif op == 2:
        n1 = int(input('Digite um Número: '))
        n2 = int(input('Digite um Número: '))
        subtra()
    elif op == 3:
        n1 = int(input('Digite um Número: '))
        n2 = int(input('Digite um Número: '))
        divi()
