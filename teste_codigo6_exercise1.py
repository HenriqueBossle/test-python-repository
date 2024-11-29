'''Cálculo de média: Escreva um programa que leia três notas e calcule a média do aluno. Se a
média for maior ou igual a 7, exiba a mensagem "Aprovado". Caso contrário, exiba
"Reprovado".'''

nota1 = float(input('Digite sua primeria nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))

media = (nota1+nota2+nota3)/3

if media >= 7:
    print('Aprovado')

else:
    print('Reprovado')