#Desenvolva um gerador de tabuada:

contador = 0
num = int(input('Digite um número: '))
while contador <= 10:
    print(f'{num} X {contador} = {num * contador}')
    contador += 1
