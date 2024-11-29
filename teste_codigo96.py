#deixe todos os valores da lista formatados em letra maiúscula e sem espaços (use funções)

produtos = ['ABC123', 'abd012', ' ABS111', 'abB222']

"""texto = 'abd012'
texto2 = ' ABS111'
texto3 = 'abB222'

texto1 = texto1.upper()
texto2 = texto2.strip()
texto3 = texto3.upper()

print(texto1)
print(texto2)
print(texto3)"""

def tratar_texto(texto):
    texto = texto.upper()
    texto = texto.strip()
    return(texto)

"""texto = 'abd012'"""
"""texto = tratar_texto(texto)"""
"""print(texto)"""

for i, produto in enumerate(produtos):
   produtos[i] = tratar_texto(produto)

print(produtos)