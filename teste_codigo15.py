'''Faça um algoritmo que calcule o desconto de um produto com base em sua porcentagem de
desconto e imprima o preço final'''

preco_inicial = float(input('Digite o preço sem desconto: R$'))

desconto = float(input('Digite o desconto (em porcentagem): '))

preco_final = preco_inicial - (preco_inicial*desconto/100)

print(f'O produto que custava R${preco_inicial:.2f} passou a custar R${preco_final:.2f}, devido a ter um desconto de {desconto:.0f}%')