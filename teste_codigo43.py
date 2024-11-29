"""Controle de Gastos Pessoais: Escreva um programa para ajudar as pessoas a controlar seus gastos
mensais. O programa deve permitir que o usuário registre seus gastos em diferentes categorias (por
exemplo, alimentação, transporte, moradia) e calcule o total gasto em cada categoria e o total geral."""

total_gastos = 0
alimentacao = 0 
transporte = 0
moradia = 0

while True:

    print('''Controlador de gastos mensais
        ******MENU******
         1 - ALIMENTAÇÃO:
         2 - TRANSPORTE: 
         3 - MORADIA:
         4 - TOTAL DE GASTOS:
         5 - SAIR''')
    opc = int(input('Escolha uma opção: '))
    if opc == 1:
        gasto = int(input('Digite o valor do gasto: '))
        alimentacao += gasto
        total_gastos += gasto
    elif opc == 2:
        gasto = int(input('Digite o valor do gasto: '))
        transporte += gasto
        total_gastos += gasto
    elif opc == 3:
        gasto = int(input('Digite o valor do gasto: '))
        moradia += gasto
        total_gastos += gasto
    elif opc == 4:
        print(f'total de gastos {total_gastos}, alimentação {alimentacao}, transporte {transporte} ,moradia {moradia}')
    elif opc == 5:
        print('Saindo...')
        break
    else:
        print('Digite uma opção valida')
    
        


