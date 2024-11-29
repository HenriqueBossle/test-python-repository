#Faça um programa que leia 5 números e informe o maior número.

lista = []
for num in range(1, 6):
    num = int(input('Digite um número: '))
    lista.append(num)
print(f'O maior valor foi: {max(lista)}')
    