"""Conversão de Moedas: Crie um programa que converta um valor em reais para dólares. O usuário
deve fornecer o valor em reais e a cotação atual do dólar."""

cotacao_dolar = float(input('Digite a cotação do dolar: '))
real = float(input('Digite o valor em real: '))

real = real * cotacao_dolar

print(f'O valor em dolar é {real:.2f}')
