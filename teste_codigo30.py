"""Cálculo de média: Escreva um programa que leia três notas e calcule a média do aluno. Se a
média for maior ou igual a 7, exiba a mensagem "Aprovado". Caso contrário, exiba
"Reprovado"."""

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3)/3

if media >= 7:
    print(f'Voce foi aprovado sua nota média foi {media:.2f}, parabéns!!!')
else:
    print(f'Você foi reprovado sua nota média foi {media:.2f}, não desista!')

