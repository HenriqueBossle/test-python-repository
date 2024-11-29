"""Durante uma campanha de doações, os Pythonistas foram incumbidos de categorizar os itens doados
(representados por números inteiros) em três listas diferentes: itens pares, itens ímpares e itens múltiplos
de 3 e 5 simultaneamente."""

lista_pares = []
lista_impares = []
lista_multiplos = []

while True:
    item = int(input("Digite um item: "))

    if item == 0:
        break

    elif item %3 == 0 and item %5 == 0:
        lista_multiplos.append(item)
        print(lista_multiplos)

    elif item %2 == 0:
        lista_pares.append(item)
        print(lista_pares)

    else:
        lista_impares.append(item)
        print(lista_impares)
    