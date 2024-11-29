"""Verificação de números pares: Escreva um programa que leia um número inteiro e verifique
se ele é par ou ímpar. Se for par, exiba a mensagem "O número é par". Caso contrário, exiba
"O número é ímpar"."""

num = int(input('Digite um número: '))

if num%2 == 0:
    print('É par')
else:
    print('É ímpar')