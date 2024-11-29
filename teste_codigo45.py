"""Faça um algoritmo que calcule a distância percorrida por um veículo com base em sua velocidade e
tempo de percurso informados pelo usuário e imprima o resultado."""

velocidade = int(input('Digite a velocidade em km/h: '))

tempo_percurso = int(input('Digite o tempo de percurso em h: '))

distancia_percorrida = velocidade * tempo_percurso

print(f'Como a velocidade foi de {velocidade} km/h e o tempo de percurso {tempo_percurso} h, a distância percorrida foi {distancia_percorrida} km')