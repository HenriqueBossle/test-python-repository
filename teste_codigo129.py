"""Crie um programa que leia um texto e conte a frequência de cada palavra, ignorando letras maiúsculas e minúsculas. Exiba o resultado em ordem decrescente de frequência."""

from collections import Counter

texto = input('Digite um texto: ').upper()
texto_lista = texto.split()

verificar = len(texto_lista)
print(verificar)
print(texto_lista)


