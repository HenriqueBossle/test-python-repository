#Elaborar um programa Python para calcular o fatorial de um número.

def fatorial(num):
    fatorial = 1
    for i in range(2, num + 1):
        fatorial = fatorial * i
    return fatorial

num = int(input('Digite um número: '))
print(fatorial(num))