#exibir data

from datetime import datetime


data_atual = datetime.now()

print(f'Agora são {data_atual.hour} horas do dia {data_atual.day} do {data_atual.month} de {data_atual.year}')
