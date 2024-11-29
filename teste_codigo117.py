#Elaborar um programa Python para calcular o fatorial de um número.

num = int(input('Digite um número: '))

contador = num
fatorial = 1

while contador > 0:
    fatorial = fatorial * contador
    contador = contador - 1

print(fatorial)

