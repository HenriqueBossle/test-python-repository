#Faça um programa que leia 5 números e informe a soma e a média dos números.

lista = []
for num in range(1, 6):
    num = int(input('Digite um número: '))
    lista.append(num)
print(sum(lista))
media = (sum(lista) / len(lista))
print (media)
  