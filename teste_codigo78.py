#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

populacao_a = int(input('Insira a população do país A: '))
populacao_b = int(input('Insira a população do país B: '))
ano = 0

taxa_crescimento_a = float(input('Insira a taxa de cresimento do país A (em decimal): '))
taxa_crescimento_b = float(input('Insira a taxa de cresiemnto do país B (em decimal): '))

while populacao_b > populacao_a:
    populacao_a = populacao_a + populacao_a * taxa_crescimento_a
    populacao_b = populacao_b + populacao_b * taxa_crescimento_b
    ano = ano + 1
print (f'Foram {ano} anos')
