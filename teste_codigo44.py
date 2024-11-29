"""Faça um algoritmo que calcule o desconto de um produto com base em sua porcentagem de
desconto e imprima o preço final"""

valor_inicial = float(input('Digite o preço inicial: '))

desconto = float(input('Digite a porcentagem de desconto (sem o %): '))

valor_final = valor_inicial - (valor_inicial*desconto//100)

print(valor_final)