print(f'------------------ Tabuada Super -----------------')
print('--=--'*10)

while True:
    num = int(input('Digite um Número para ver a sua Tabuada: '))

    if num == 0:
        print('Saindo do Programa...')
        break
    # Fazendo a Tabuada
    for c in range(1, 13):
        print(f'{num} x {c:2} = {num*c}')
