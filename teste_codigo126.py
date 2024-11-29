#Crie um programa que permita ao usuário adicionar, remover e listar tarefas. Utilize funções para cada operação: adicionar_tarefa(tarefa), remover_tarefa(tarefa), e listar_tarefas(). Utilize uma lista para armazenar as tarefas.

lista_tarefas = []

def adicionar_tarefa(tarefa):
    lista_tarefas.append(tarefa)
    print(f'A tarefa "{tarefa}" foi adicionada com sucesso!!!')

def remover_tarefa(tarefa):
    if tarefa in lista_tarefas:
        lista_tarefas.remove(tarefa)
        print(f'A tarefa "{tarefa}" foi removida com sucesso!')
    else:
        print(f'A tarefa "{tarefa}" não encontrada na lista de tarefas!')

def listar_tarefas():
    if lista_tarefas:
        print('Lista de tarefas: ')
        for i, tarefa in enumerate(lista_tarefas, 1):
            print(i, tarefa)
        else:
            print('A lista de tarefas está vazia')


while True:
    print('''MENU
        1 - ADICIONAR TAREFA
        2 - REMOVER TAREFA
        3 - LISTAR TAREFAS
        4 - SAIR DO SISTEMA''')

    opc = int(input('Escolha uma opção: '))

    if opc == 1:
        tarefa = input('Digite uma tarefa: ')
        adicionar_tarefa(tarefa)

    if opc == 2:
        tarefa = input('Informe a tarefa que quer remover: ')
        remover_tarefa(tarefa)

    if opc == 3:
        listar_tarefas()
    
    if opc == 4:
        print('Você saiu!')
        break