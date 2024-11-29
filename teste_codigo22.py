import math

#Um triângulo equilátero tem lado de medida 6cm. Calcule a sua área.
#(l**2*raiz de 3)/4

l = int(input('Insira o valor do lado: '))

area = l**2 * math.sqrt(3) / 4

print(area)