"""Verificação de idade: Escreva um programa que peça a idade do usuário e verifique se ele é
maior de idade ou não. Se for maior de idade, exiba a mensagem "Você é maior de idade".
Caso contrário, exiba "Você é menor de idade"."""

idade = int(input('Qual é a sua idade? '))

if idade >= 18:
    print('Você é MAIOR de idade')
else:
    print('Você é MENOR de idade')