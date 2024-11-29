"""Um ônibus saiu de uma cidade a 300km de distância e foi até outra cidade a uma
velocidade média de 60km/h. Quanto tempo ele levou para chegar ao destino?"""

distancia = int(input('Digite a distância em km: '))
velocidade_media = int(input('Digite a velocidade média em km/h: '))
 
tempo = distancia // velocidade_media

print(f'O ônibus levou {tempo} horas para chegar ao seu destino')

