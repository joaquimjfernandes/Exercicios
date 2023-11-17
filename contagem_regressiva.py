import datetime
import time


def countdown():
    hoje = datetime.datetime.now()
    ano = hoje.year
    proximo_ano = datetime.datetime(ano + 1, 1, 1)
    tempo_restante = proximo_ano - hoje

    while tempo_restante.total_seconds() > 0:
        dias = tempo_restante.days
        hora, resto = divmod(tempo_restante.seconds, 3600)
        minutos, segundos = divmod(resto, 60)

        print(f'Restam {dias}dias, {hora}hora, {minutos}minutos, {segundos}segundos para o Final de Ano')

        # Atualização da Hora e os Minutos
        hoje = datetime.datetime.now()
        tempo_restante = proximo_ano - hoje

        time.sleep(1)
    print('Happy New Year to EverOne!!!')

countdown()