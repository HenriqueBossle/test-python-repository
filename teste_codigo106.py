"""Durante uma campanha de doações, os Pythonistas foram incumbidos de categorizar os itens doados
(representados por números inteiros) em três listas diferentes: itens pares, itens ímpares e itens múltiplos
de 3 e 5 simultaneamente."""

pares = []
impares = []
multiplos = []

while True:
    item_doado = int(input('Digite o item doado: '))

    if item_doado % 2 == 0:
        pares.append(item_doado)
        print(pares)  

    elif item_doado % 2 != 0:
        impares.append(item_doado)
        print(impares)

    if item_doado % 3 == 0 and item_doado % 5 == 0:
        multiplos.append(item_doado)
        print(multiplos)
    
    elif item_doado == 0:
        break
