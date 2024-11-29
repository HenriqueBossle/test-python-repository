"""Escreva um programa que receba uma lista de números do usuário e imprima a
lista em ordem crescente."""

lista = []
while True:
    num = input('Digite um número inteiro: ')
    if num == 'sair':
        break
    lista.append(int(num))
    lista.sort(reverse=False)
    print(lista)


