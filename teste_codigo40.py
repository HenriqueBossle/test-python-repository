"""Decomposição de Valor em Notas e Moedas: Desenvolver um programa em Python que receba um
valor em reais do usuário e decomponha esse valor no menor número possível de notas de R$ 100, R$
50, R$ 20, R$ 10, R$ 5, R$ 2 e moedas de R$ 1.
Exemplo de saída:
Digite o valor em reais: 439
Notas de R$100: 4
Notas de R$50: 0
Notas de R$20: 1
Notas de R$10: 1
Notas de R$5: 1
Notas de R$2: 2
Moedas de R$1: 0"""
valor = int(input('Digite um valor para decompor: '))

cem = valor//100
print(f'Notas de cem {cem}')
resto = valor%100
#print(resto)

cinquenta = resto//50
print(f'Notas de cinquanta {cinquenta}')
resto = resto%50
#print(resto)

vinte = resto//20
print(f'Notas de vinte {vinte}')
resto = resto%20
#print(resto)

dez = resto//10
print(f'Notas de dez {dez}')
resto = resto%10
#print(resto)

cinco = resto//5
print(f'Notas de cinco {cinco}')
resto = resto%5
#print(resto)

dois = resto//2
print(f'Notas de dois {dois}')
resto = resto%2
#print(resto)

um = resto//1
print(f'Moedas de um {um}')
resto = resto%1
#print(resto)
