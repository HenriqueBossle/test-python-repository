'''Faça um algoritmo que calcule o desconto de um produto com base em sua porcentagem de
desconto e imprima o preço final.'''

valor_cheio = float(input('Digite o preço sem desconto: R$'))

porcentagem_de_desconto = float(input('Insira a porcentagem de desconto (só o número, sem o "%"): '))

valor_final = valor_cheio-(valor_cheio*porcentagem_de_desconto/100)

print(f'Um produto que custava R${valor_cheio} com desconto de {porcentagem_de_desconto}% passou a custar R${valor_final:.2f}')

