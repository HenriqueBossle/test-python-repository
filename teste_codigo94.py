"""Calculadora de Consumo de Combustível: Escreva um programa que calcule o consumo médio de
combustível de um veículo. O usuário deve informar a quantidade de combustível gasta e a distância
total percorrida."""

print('Consumo de Combustível')

qtd_gasta = int(input('Digite a quantidade gasta de combustível: '))
distancia = int(input('Digite a distância total percorrida: '))

consumo = distancia // qtd_gasta

print(consumo)