"""1) Um programa de computador precisa verificar se um número digitado pelo usuário é positivo,
negativo ou zero. Escreva um programa que leia um número e imprima uma mensagem
informando se ele é positivo, negativo ou zero.(0,25)"""

num = int(input('Digite um número: '))

if num > 0:
    print('POsitivo')
elif num < 0: 
    print('negativo')
else:
    print('Zero')

