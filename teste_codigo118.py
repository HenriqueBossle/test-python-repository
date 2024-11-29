#Elaborar um programa Python para calcular o fatorial de um número.

num = int(input('Digite um número: '))

fatorial = 1
for i in range(2,num + 1):
    fatorial = fatorial * i
print(fatorial)