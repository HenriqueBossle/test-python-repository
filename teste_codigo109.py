"""Faça um programa que tenha uma função chamda escreva(), que receba um texto qualquer como parametro e mostre uma mensagem com tamnaho adpatavel"""
def escreva(msg):
    tam = len(msg) + 2
    print('~'*tam)
    print(f' {msg}')
    print('~'*tam)

escreva(input('Escreva algo: '))
