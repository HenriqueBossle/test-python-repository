#Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))

for item in range(num1 + 1, num2):
  print(item) 

for item in range(num2 + 1, num1):
  print(item)

soma = item + item

print(f'A soma dos números entre {num1} e {num2} é igual a {soma}')