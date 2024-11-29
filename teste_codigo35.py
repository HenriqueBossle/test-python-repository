"""Você está desenvolvendo um programa que verifica se um número é par ou ímpar. Para isso, você
precisa solicitar o número e verificar se ele é divisível por 2. Se o número for divisível por 2, o
programa deve informar que o número é par, caso contrário, o programa deve informar que o número
é ímpar."""

num = int(input('Insira um número: '))

if num%2 == 0:
    print('O número é par')
else:
    print('O número e ímpar')