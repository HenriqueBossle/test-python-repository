"""Calculadora de Consumo de Combustível: Escreva um programa que calcule o consumo médio de
combustível de um veículo. O usuário deve informar a quantidade de combustível gasta e a distância
total percorrida."""

quantidade_gasta_combustivel = int(input('Digite a quantidade de combustivel gasta: '))

distancia_percorrida = int(input('Digite a distancia percorrida em km: '))

consumo = distancia_percorrida // quantidade_gasta_combustivel

print(consumo)