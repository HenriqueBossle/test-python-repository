'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''

nome = input('Digite seu nome: ')
while len(nome) <= 3:
    nome = input('Digite seu nome novamente (maior que 3 caracteres): ')

idade = int(input('Informe sua idade: '))
while idade < 1 or idade >150:
    idade = int(input('Informe sua idade novamente (1 até 150 anos):'))

salario = int(input('Informe seu salário: R$'))
while salario <=0:
    salario = int(input('Informe seu salário (acima de R$0): R$'))

sexo = input('Qual o seu sexo f ou m: ')
while sexo != 'f' and sexo != 'm':
    sexo = input('Digite seu sexo f OU m: ')

estado_civil = input('Informe seu estado civil "s" para solteiro(a), "c" para casado(a) , "v" para viúvo(a), "d" para divorciado(a): ')
while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    estado_civil = input('Informe seu estado civil novamente "s" para solteiro(a), "c" para casado(a) , "v" para viúvo(a), "d" para divorciado(a):') 
print('Você completou o questionário !!!')




    
    

