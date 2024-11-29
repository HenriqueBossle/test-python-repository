"""Você está desenvolvendo um programa para calcular a corrente elétrica em um circuito elétrico. O
usuário deve informar a resistência elétrica e a tensão elétrica do circuito. Escreva um algoritmo que
calcule e imprima a corrente elétrica do circuito, de acordo com a lei de Ohm."""

t = int(input('Digite a tensão elétrica: '))
r = int(input('Digite a resistência elétrica: '))

corrente = t / r 

print(f'A corrente elétrica é {corrente:.2f}')