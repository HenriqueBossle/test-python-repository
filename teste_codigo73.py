""""Escreva um programa que solicita ao usuário que digite um número inteiro positivo. O
programa deve imprimir todos os números de 1 até o número digitado pelo usuário que são
múltiplos de 2, usando um loop while.
"""

numero = int(input("Digite um número inteiro positivo: "))
if numero > 0:
    contador = 1
    while contador <= numero:
        if contador % 2 == 0:
            print(contador)
        contador += 1
else:
    print("Por favor, digite um número inteiro positivo.")

