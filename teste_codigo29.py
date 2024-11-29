"""Uma pessoa tem R$ 500 em sua conta corrente e precisa pagar uma conta de R$ 150 e
outra de R$ 300. Qual é o saldo final da conta corrente? """

conta_corrente = int(input('Digite o valor na conta corrente: R$'))

conta_a_pagar1 = int(input('Digite o valor da conta para pagar: R$'))

conta_a_pagar2 = int(input('Digite o valor da segunda conta para pagar: R$'))

saldo_final = conta_corrente - (conta_a_pagar1 + conta_a_pagar2)

print(f'O valor na sua conta corrente era R${conta_corrente} como a primeira conta custava R${conta_a_pagar1} e a segunda R${conta_a_pagar2} o saldo final na conta corrente foi de R${saldo_final}')