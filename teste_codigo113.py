# Calculadora Básica

while True:
    print("Escolha uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("0. Sair")
    
    opc = input("Digite a sua opção: ")
    
    if opc == '0':
        break
    
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if opc == '1':
        resultado = num1 + num2
        print(f"O resultado da adição é: {resultado}")
    elif opc == '2':
        resultado = num1 - num2
        print(f"O resultado da subtração é: {resultado}")
    elif opc == '3':
        resultado = num1 * num2
        print(f"O resultado da multiplicação é: {resultado}")
    elif opc == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f"O resultado da divisão é: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    else:
        print("Opção inválida. Tente novamente.")

#Com Funções:
# Funções para operações básicas
def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero não é permitida."

def menu():
    print("Escolha uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("0. Sair")

# Loop principal
while True:
    menu()
    opc = input("Digite a sua opção: ")
    
    if opc == '0':
        break
    
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if opc == '1':
        print(f"O resultado da adição é: {adicao(num1, num2)}")
    elif opc == '2':
        print(f"O resultado da subtração é: {subtracao(num1, num2)}")
    elif opc == '3':
        print(f"O resultado da multiplicação é: {multiplicacao(num1, num2)}")
    elif opc == '4':
        print(f"O resultado da divisão é: {divisao(num1, num2)}")
    else:
        print("Opção inválida. Tente novamente.")