"""Uma loja de roupas está com uma promoção de 20% de desconto em todos os produtos.
Uma blusa custava R$ 80, quanto ela custará agora?"""

custo_inicial = int(input('Insira o custo incial: R$'))
desconto = int(input('Insira o desconto em porcentagem: '))

custo_final = custo_inicial - (custo_inicial * desconto // 100)

print(f'O custo final da blusa com desconto foi de: R$ {custo_final}')