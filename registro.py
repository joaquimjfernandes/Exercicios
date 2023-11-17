while True:
    pessoas = []
    for p in range(1, 5):
        print(f'-------- {p}ª Pessoa --------')
        nome = str(input('Nome Completo: '))
        genero = str(input('Genero: '))
        nac = str(input('Nacionalidade: '))
        idade = int(input('Idade: '))
        est_civil = str(input('Estado Cívil: '))

        print(f'Com tudo foram cadastrado {p} Pessoas')
