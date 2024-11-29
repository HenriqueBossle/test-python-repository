"""Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere P, se seu argumento for positivo, e N, se seu argumento for zero ou negativo."""

def valorarg(arg1):
    if arg1 >= 1:
        return 'Positivo'
    elif arg1 < 0:
        return 'Negativo'
    elif arg1 == 0:
        return 'Neutro'

num = int(input('Digite um valor: '))

verificação = valorarg(num)

print(verificação)


