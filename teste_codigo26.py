"""Uma loja de brinquedos está com uma promoção de 30% de desconto em um boneco que
custa R$ 60. Qual é o preço do boneco com desconto?"""

custo_inicial = int(input('Digite o custo inicial: '))

desconto = int(input('Digite o desconto: '))

custo_final = custo_inicial - (custo_inicial * desconto // 100)

print(custo_final)