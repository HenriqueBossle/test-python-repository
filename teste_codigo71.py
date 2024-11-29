"""Escreva um programa que leia 10 números reais e informe a média dos elementos """

lista = []
while True:
    num = input('Digite um número: ')
    if num == 'sair':
        break
    lista.append(int(num))
    print(lista)

soma = sum(lista)
contagem = len(lista)
media  = soma / contagem
print(media)
    
    
    