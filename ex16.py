# Ler um valor e escrever a mensagem É MAIOR QUE 10! se o valor lido for maior que 10, caso
# contrário escrever NÃO É MAIOR QUE 10!

numero = int(input('Digite um Número: '))
if numero > 10:
    print(f'O Número {numero} é MAIOR que 10!')
elif numero == 10:
    print(f'O Número {numero} não é MAIOR que 10, MAS É IGUAL a 10!')
else:
    print(f'O Número {numero} não é MAIOR que 10!')
