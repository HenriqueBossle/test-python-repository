"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num = input('Digite um número inteiro: ')


if num%2 == 0:
    print('O número é par')

elif num%2 != 0:
    print('O número é ímpar')

else:
    print('Isso não é um número inteiro')