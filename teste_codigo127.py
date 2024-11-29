#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
print(f"A frase digitada foi {junto}")
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)

if inverso == junto:
    print("É um palindromo")
else: 
    print("Não é um palindromo")
