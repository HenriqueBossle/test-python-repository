"""A biblioteca de TechVille queria reorganizar seus livros segundo o número de páginas dos livros, tanto em
ordem crescente quanto decrescente. Os Pythonistas foram chamados para desenvolver um programa que
recebesse a lista de números de páginas e ordenasse conforme necessário."""

num_pag_lista = [123,156,260,302,230,314,311,297,293,301]

num_pag_lista.sort(reverse=False)

print(f'Essa é a lista em ordem crescente: {num_pag_lista}')

num_pag_lista.sort(reverse=True)

print(f'Essa é a lista em ordem decresente: {num_pag_lista}')