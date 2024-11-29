"""2. Escreva um programa que receba uma lista de nomes do usuário e imprima cada
nome em uma linha separada"""

lista = []
while True:
    nome = input('Digite um nome: ')
    if nome == 'sair':
        break
    lista.append(nome)
    print(lista)
    
for nome in lista:
    print(lista)
