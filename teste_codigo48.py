"""Ana é uma professora de matemática que está desenvolvendo um programa para calcular a média
aritmética de uma lista de números. Ela sabe que, para calcular a média, é necessário somar todos
os números da lista e dividir pelo total de números. Ana quer desenvolver um programa em Python
que possa ser utilizado por seus alunos para facilitar esse processo. Escreva um algoritmo que ajude
Ana a calcular a média aritmética de uma lista de números."""

numeros = [1,2,3,4,5]

soma = sum(numeros)
#print(soma)
contador = len(numeros)
#print(contador)

media = soma // contador

print(media)