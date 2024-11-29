"""Um jardineiro está plantando uma cerca viva que tem 25 metros de comprimento. Se ele
precisa plantar uma muda a cada 50 centímetros, quantas mudas ele precisará?"""
'''Quantidade de mudas = área do canteiro em m² / área ocupada pela muda em m²'''

comprimento_cerca_em_m = 25

espaçamento_entre_mudas_em_cm = 50
espaçamento_entre_mudas_em_m = 0.5

quantidade_de_mudas = comprimento_cerca_em_m / espaçamento_entre_mudas_em_m

print(quantidade_de_mudas)