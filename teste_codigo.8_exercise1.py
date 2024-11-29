'''Você está desenvolvendo um programa para calcular a corrente elétrica em um circuito elétrico. O
usuário deve informar a resistência elétrica e a tensão elétrica do circuito. Escreva um algoritmo que
calcule e imprima a corrente elétrica do circuito, de acordo com a lei de Ohm.'''

#tensão = voltagem

t = int(input('Digite a tensão eletrica: '))

r = int(input('Digite a resistência eletrica: '))

c = t / r

print(f'A corrente elétrica foi de {c}')