# Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.
print('=================== ORDEM CRESCENTE DOS VALORES ===================')

v3 = int(input('Digite um Valor: '))
v4 = int(input('Digite outro Valor: '))
if v3 > v4:
    p = v4
    s = v3
    print(f'OS NÚMEROS EM ORDEM CRESCENTE SÃO -> {p} e {s}')
elif v4 > v3:
    p = v3
    s = v4
    print(f'OS NÚMEROS EM ORDEM CRESCENTE SÃO -> {p} e {s}')