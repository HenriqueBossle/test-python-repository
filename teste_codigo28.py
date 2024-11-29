"""uma pessoa está organizando uma festa e precisa de 1,5 litros de refrigerante para cada
convidado. Se ela convidou 30 pessoas, quantos litros de refrigerante ela precisará?"""

litros_por_pessoa = float(input("Digite o valor de litros por pessoa: "))

num_de_pessoas = float(input('Digite o número de convidados: '))

total_de_refri = litros_por_pessoa * num_de_pessoas

print(f'Para a festa são necessarios {total_de_refri:.0f} litros de refri.')