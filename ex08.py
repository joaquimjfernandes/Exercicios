# Media de um Aluno @joaquim fernandes
print('-'*30)
print('     Boletim do Estudante')
print('-'*30)

# Recebendo todos os Valores
nomeAluno = str(input('Digite o seu Nome: '))
curso = str(input('Digite o seu Curso: '))
nota1 = float(input(f'Digite a Primeira Nota: '))
nota2 = float(input(f'Digite a Segunda Nota: '))
nota3 = float(input(f'Digite a Terceira Nota: '))
nota4 = float(input(f'Digite a Quarta Nota: '))
print('-'*15)

# Fazendo a Soma e a Divisão
media = (nota1 + nota2 + nota3 + nota4) / 4

# Fazendo as Condições
if media >= 11:
    print(f'O Estudante {nomeAluno}, Aprovou com {media} no Curso de {curso}!')
elif media <= 10:
    print(f'O Estudante {nomeAluno}, fará o Exame Especial com a media de {media}')
    exame = float(input('Digite a Nota do Exame:'))
    novaMedia = exame
    if novaMedia > 10:
        print(f'O Estudante {nomeAluno}, Aprovou no Exame com a Média de -> {media}!')
    elif novaMedia < 10:
        print(f'O Estudante {nomeAluno}, Reprovou com {media} no Curso de {curso}!')
else:
    print(f'O Estudante {nomeAluno}, Reprovou com {media} no Curso de {curso}!')
