def funcao(msg = 'olá', nome= 'usuário'):
    msg = msg.replace('o', '0',)
    nome = nome.replace('o', '0',)
    return f'{msg} {nome}'

variavel = funcao()

print(variavel)