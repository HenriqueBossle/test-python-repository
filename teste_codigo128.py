#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = str(input('Digite uma frase: ')).upper()
palavras = frase.split()
juntas = ''.join(palavras)
palavra_invertida = juntas[::-1]

print(juntas)
print(palavra_invertida)

if juntas == palavra_invertida:
    print("É um palimdromo")

else:
    print("Não é")