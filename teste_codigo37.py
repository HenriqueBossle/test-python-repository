"""Maria é uma estudante de física que está desenvolvendo um programa para converter uma
temperatura de Celsius para Fahrenheit. Ela sabe que muitas vezes precisa realizar essa conversão
em seus estudos, mas a fórmula matemática pode ser confusa. Por isso, ela está desenvolvendo um
programa em Python que simplifica esse processo. Escreva um algoritmo que ajude Maria a
converter uma temperatura de Celsius para Fahrenheit."""

celsius = float(input('Digite a temperatura em celsius: '))

fahrenheit = 32 + (9/5)*celsius

print(fahrenheit)