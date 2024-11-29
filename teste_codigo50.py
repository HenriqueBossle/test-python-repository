
"""Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a quantidade de caracteres da str"""

variavel = "Olá Mundo"

#seleção de elemento da string
print(variavel[0])
print(variavel[1])
print(variavel[2])
print(variavel[3])
print(variavel[4])
print(variavel[5])
print(variavel[6])
print(variavel[7])
print(variavel[8])

#fatiamento
print(variavel[0:5])
print(variavel[-5:-3])

#contagem de caracteres
print(len(variavel))
print(len(variavel[2]))


