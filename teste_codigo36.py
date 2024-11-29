"""Você está desenvolvendo um programa para classificar triângulos de acordo com as medidas de
seus lados. O usuário deve informar as medidas dos três lados do triângulo. Escreva um algoritmo
que determine e imprima se o triângulo é equilátero, isósceles ou escaleno."""

lado1 = int(input('Digite o primeiro lado: '))
lado2 = int(input('Digite o segundo lado: '))
lado3 = int(input('Digite o terceiro lado: '))

if lado1 == lado2 == lado3:
    print('EQUILÁTERO')
elif lado1 == lado2 != lado3:
    print('ISÓCELES')
elif lado1 != lado2 == lado3:
    print('ISÓCELES')
else:
    print('ESCALENO')