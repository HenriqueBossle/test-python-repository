"""Escreva um programa que receba uma lista de números do usuário e imprima
apenas os números ímpares presentes na lista em ordem decrescente."""

lista = []
while True:
    num = int(input('Digite um número: '))
    if num%2 != 0:
        lista.append(num)
        lista.sort(reverse=True)
        print(lista)
        

    
