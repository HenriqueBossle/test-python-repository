#calculadora while

while True:
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    operador = input('Digite o operador(+,-,x,/): ')
    operddores_permitidos = '+-x/'

    if operador not in operddores_permitidos:
        print('Digite um operador valido')
        continue
         
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    if operador == '+':
        print(f'{num1 + num2}')

    elif operador == '-':
        print(f'{num1 - num2}')

    elif operador == 'x':
        print(f'{num1 * num2}')

    elif operador == '/':
        print(f'{num1 / num2}')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair == True:
        break
