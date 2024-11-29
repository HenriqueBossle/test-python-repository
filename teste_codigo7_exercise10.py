'''Verificação de vogal: Escreva um programa que leia uma letra e verifique se ela é uma vogal
ou não. Se for uma vogal, exiba a mensagem "A letra é uma vogal". Caso contrário, exiba "A
letra é uma consoante".'''


letra = input('Digite uma letra: ').upper()

vogal = ['A','E','I','O','U']


if letra in vogal:
    print(f'A letra {letra} é vogal')
else:
    print(f'A letra {letra} não é vogal')
