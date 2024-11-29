#listas
import math

lista = []

while len(lista) < 3:
    notas = float(input('Digite sua nota: '))

    lista.append(notas)



    soma = sum(lista)
    contagem = len(lista)
    media = soma/contagem
    
    print(f'Media final {media:.2f}')

    if media >= 6:
        print('aprovado')

    else:
        print('reprovado')


    