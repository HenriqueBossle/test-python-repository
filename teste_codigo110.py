"""Faça um programa que leia as medidas da base a altura de um retangulo. apos ler esses valores o algoritimo deve chamar uma função que recebe as medidas calcula o perimetro o retangulo e retonra o resultado. Na sequência o algoritimo deve passar esses valores como parametros para uma função que calcula a area do retangulo e retorna o resultado""" 

def perimetro(base, altura):
    p = base + altura + base + altura
    return p

def area(base, altura):
    a = base*altura
    return a 

b = 2
a = 4
per = perimetro(b, a)
ar = area(b, a)
print(f'Perímetro é {per}')
print(f'Altura é {ar}')