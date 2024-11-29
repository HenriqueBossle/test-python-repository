"""Conversão de Inteiro para Binário: Desenvolver um programa em Python que converta um número
inteiro fornecido pelo usuário em sua representação binária.
Descrição:
O programa deve solicitar ao usuário que insira um número inteiro.
O programa deve então converter esse número inteiro em sua representação binária """

num = int(input('Digite um número: '))

num = bin(num)
print(num[2::])


