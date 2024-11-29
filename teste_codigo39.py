"""Algoritmo de Tabuada: Desenvolver um programa em Python que permita ao usuário calcular a
tabuada de qualquer número inteiro. O programa deve solicitar ao usuário que insira um número e, em
seguida, exibir a tabuada correspondente de 1 a 10."""

num = int(input('Digite um número: '))
contador = 1
while contador <= 10:
    print(f'{num} X {contador} = {num * contador}')
    contador += 1
    
    