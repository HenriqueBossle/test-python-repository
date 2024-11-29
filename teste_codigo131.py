"""Imagine que você está desenvolvendo um sistema de inventário para uma pequena loja. Você recebeu uma lista de produtos com seus preços, e sua tarefa é ordená-los de diferentes maneiras para exibição.
Crie uma lista chamada produtos que contenha os seguintes itens, cada um como um dicionário com as chaves 'nome' e 'preco':"""
"""Ordene a lista de produtos em ordem crescente de preços. Utilize o método sort() e a chave de ordenação apropriada. Exiba a lista ordenada."""

lista_produtos = [{'nome': 'camiseta', 'preço' : 50},
                  {'nome': 'chapeu', 'preço' : 30},
                  {'nome': 'calça', 'preço' : 80},
                  {'nome': 'jaqueta', 'preço' : 150}
                  ]

lista_produtos.sort(key=lambda produto: produto['preço'])
print(lista_produtos)
