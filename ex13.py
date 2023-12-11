#  Peça para o usuário digitar a sua idade. Exiba se ele é obrigado a votar, se é proibido
# de votar ou se o voto é obrigatório

nome = input('Qual é o seu Nome: ')
idade = int(input('Quantos Anos Tens: '))

if idade <= 17:
    print(f'Senhor {nome}, Ainda não tens o Direito de Votar!')
elif 18 <= idade < 65:
    print(f'Senhor {nome}, Já Tens Idade para Votar!')
elif idade >= 65:
    print(f'senhor {nome}, O seu Voto Agora é Opcional!')
