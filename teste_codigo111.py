"""Fqça um programa que tenha uma funções chamda área() que receba as dimensões de um terreno (largura e comprimento) e mostre a área do terreno"""

def area(largura, comprimento):
    a = largura * comprimento
    print(f'A area do terreno é {a:.2f}')
l = float(input('Digite a largura do terreno: '))
c = float(input('Digite o comprimento do terreno: '))
area(l,c)