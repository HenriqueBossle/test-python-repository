""""Escreva um programa que solicita ao usuário que digite um número inteiro positivo. O
programa deve imprimir todos os números de 1 até o número digitado pelo usuário que são
múltiplos de 2, usando um loop while. """

num = int(input('Digite um número: '))
if num > 0:
    contador = 1
    while contador <= num:
        if contador % 2 == 0:
          print(contador)
    contador += 1

