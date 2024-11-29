"""Você está desenvolvendo um programa para calcular a distância percorrida por um objeto em um
movimento uniformemente acelerado. O usuário deve informar a velocidade inicial, a aceleração e o
tempo de deslocamento. Escreva um algoritmo que calcule e imprima a distância percorrida pelo
objeto."""

v0 = int(input('Digite a velocidade inicial em km/h: '))

a = int(input('Escreva a aceleração: '))

t = int(input('Insira o tempo de deslocamento em h: '))

distancia_percorrida = v0 * t + 0.5 * a * t**2

print(f'A distância percorrida foi de {distancia_percorrida}')