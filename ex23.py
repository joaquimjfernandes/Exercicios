# Ler o nome de 2 times e o número de gols marcados na partida (para cada time). Escrever o nome
# do vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE.
time1 = str(input('Equipa da Casa: '))
time2 = str(input('Equipa Visitante: '))
time1Gol = int(input('Nº de Gols[Casa]: '))
time2Gol = int(input('Nº de Gols[Visitante]: '))

if time1Gol > time2Gol:
    print(f'A Equipa da Casa [{time1}] Venceu a Partida com {time1Gol}Gols')
elif time2Gol > time1Gol:
    print(f'A Equipa Visitante [{time2}] Venceu a Partida com {time2Gol}Gols')

elif time1Gol == time2Gol:
    print(f'A Partida entre {time1} x {time2} -> foi Empatada por [{time1Gol}:{time2Gol}]')
