"""Faça um algoritmo que calcule a distância percorrida por um veículo com base em sua velocidade e
tempo de percurso informados pelo usuário e imprima o resultado."""

velocidade = float(input('Digite a velocidade em km/h: '))
tempo_percurso = float(input('Informe o tempo de percurso em h: '))

distancia_percorrida = velocidade * tempo_percurso

print(f'A distância percorrida foi de: {distancia_percorrida} km')

