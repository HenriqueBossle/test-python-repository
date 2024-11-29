"""Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos."""

def soma_valores(num1, num2, num3):
    return num1 + num2 + num3

valor1 = int(input('Insira um número: '))
valor2 = int(input('Insira um número: '))
valor3 = int(input('Insira um número: '))

result = soma_valores(valor1, valor2, valor3)

print(result)


