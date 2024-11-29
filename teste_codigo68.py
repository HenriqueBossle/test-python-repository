"""Escreva um programa que receba uma lista de números do usuário e imprima a
lista em ordem decrescente."""

lista = []
while True:
    num = input('Digite um número: ')
    if num == 'sair':
        break
    lista.append(int(num))
    lista.sort(reverse=True)
    print(lista)
