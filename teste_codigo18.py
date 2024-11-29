"""Uma pessoa foi a um restaurante que está com um prato do dia que custa R$ 35, mas no
horário do almoço ele é vendido por R$ 25. Quantos reais uma pessoa economizaria pedindo o
prato do dia no horário do almoço?"""

custo_normal = int(input('Digite o custo normal: R$'))
custo_h_almoço = int(input('Digite o custo na hora do almoço: R$'))

economia = custo_normal - custo_h_almoço

print(f'A economia da pessoa que foi ao restaurante no horário do almoço foi de: R${economia}')