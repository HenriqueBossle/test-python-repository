"""Faça um programa que tenha uma função chamada maior() que receba varios parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior"""
from time import sleep

def maior(*num):
    cont = maior = 0
    print('Analisando os valores')
    for item in num:
        print(f'{item} ', end='', flush=True)
        sleep(0.2)
        if maior == 0:
           maior = item
        else:
            if item > maior:
                maior = item
        cont += 1
    print(f'- Os valores informados foram {cont}')
    print(f'O maior valor é {maior}')
    

maior(3, 5, 7, 1, 8, 9, 2)
maior(6, 8, 9, 12, 7, 78, 4)
maior(7, 8, 5, 2)
