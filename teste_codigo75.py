"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações."""

nome = input('Digite seu nome: ')
senha = input('Digite sua senha: ')
if senha != nome:
   print('Senha aceita')

while senha == nome:
    print('A senha não pode ser igual a nome de usuário, por favor digite as inofmrações novamente')
    nome = input ('Digite seu nome novamente: ')
    senha = input('Digite sua senha novamente (não pode ser igual ao nome): ')
    if senha != nome:
      print('Senha Aceita')

