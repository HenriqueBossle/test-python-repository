#Calculadora
def soma(num1, num2):
    return num1 + num2
def subtração(num1, num2):
    return num1 - num2
def multiplicação(num1, num2):
    return num1 * num2
def divisão(num1, num2):
    return num1 / num2

while True:
    print('~' * 21)
    print('''Calculadora em Python''')
    print('~' * 21)
    print('Menu')
    print('~' * 21)
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Sair')
    print('~' * 21)
    opc = int(input('Escolha uma opção: '))
    print('~' * 21)

    if opc >=1 and opc <=4:
        numero1 = int(input('Digite um número: '))
        numero2 = int(input('Digite outro número: '))
        if opc == 1:
            print(f'O resultado foi {soma(numero1, numero2)}')
        elif opc ==2:
            print(f'O resultado foi {subtração(numero1, numero2)}')
        elif opc ==3:
            print(f'O resultado foi {multiplicação(numero1, numero2)}')
        elif opc ==4:
            print(f'O resultado foi {divisão(numero1, numero2)}')
        elif opc == 5:
            print('Você Saiu!')
            print('~' * 21)
            break
    else:
        print('Digite uma opção valida')
        print('~' * 21)
