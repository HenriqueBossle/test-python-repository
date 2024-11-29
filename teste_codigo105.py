"""O mercado local queria entender melhor as vendas do mês. Eles pediram aos Pythonistas para criar um
programa que calculasse a soma, a média, o maior e o menor valor das vendas diárias."""

vendas_diarias = [1199,569,929,239,199,899]


soma = sum(vendas_diarias)
print(soma)

qtd_vendas = len(vendas_diarias)
print(qtd_vendas)

media = soma / qtd_vendas
print(f'{media:.2f}')

maior = max(vendas_diarias)
print(maior)

menor = min(vendas_diarias)
print(menor)