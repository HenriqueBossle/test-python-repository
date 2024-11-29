'''Uma pessoa trabalha em uma empresa e recebe um salário base de R$ 2.500, mas também
recebe um adicional de R$ 350 por mês por desempenho. Qual é o salário dessa pessoa em um
ano?'''

salario_base = int(input('Digite o salário base: R$ '))
adicional = int(input('Digite o adicional recebido: R$ '))

salario_mensal = salario_base + adicional
print(salario_mensal)
salario_anual = salario_mensal * 12

print(f'O salário anual deste funcionario foi de: R$ {salario_anual}')