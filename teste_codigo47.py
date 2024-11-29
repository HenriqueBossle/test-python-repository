"""Pedro é um estudante de matemática que está desenvolvendo um programa para calcular o volume
de uma esfera. Ele sabe que o cálculo pode ser um pouco complicado, mas também é muito
importante em diversas áreas da matemática e da física. Pedro está animado em desenvolver esse
programa em Python para ajudar outros estudantes a entenderem melhor a fórmula. Escreva um
algoritmo que ajude Pedro a calcular o volume de uma esfera"""

#V = 4/3 π r³

import math

r = int(input('Digite o raio em cm: '))

#divisão = 4/3

#print(divisão)

volume = (4/3) * math.pi * r**3

print(f'O volume de uma esfera de raio {r} é igual a {volume:.2f}cm³')

