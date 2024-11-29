"""Uma escola de inglês oferece um curso de 6 meses que custa R$ 2.400. Qual é o valor
mensal do curso?"""

custo_total_do_curso = int(input('Digite o custo total do curso:'))

num_de_meses = int(input('Digite o número de meses do curso: '))

valor_mensal = custo_total_do_curso // num_de_meses

print(valor_mensal)