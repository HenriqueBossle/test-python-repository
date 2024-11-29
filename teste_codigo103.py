"""Durante a feira anual de TechVille, os organizadores quiseram saber a média dos números pares dos
ingressos vendidos. Eles pediram aos Pythonistas para criar um programa que pudesse receber a lista de
todos os números dos ingressos e calcular essa média."""

lista_ingresso = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

soma_ingresso = sum(lista_ingresso)
print(soma_ingresso)

qtd_ingresso = len(lista_ingresso)

print(qtd_ingresso)

media_ingresso = soma_ingresso / qtd_ingresso

print(media_ingresso)