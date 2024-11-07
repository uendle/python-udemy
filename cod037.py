from os import system
import json
caminho='/home/uendle/Estudos/Udemy/bd.json'
lista_tarefas=[]
tarefas_desfeitas=[]
texto= '''COMANDOS: Listar, desfazer, refazer
Digite uma tarefa ou comando: '''

def listar():
    print('lista:')
    if not lista_tarefas:
        system('clear')
        print('nenhuma tarefa para listar!!!')
        return
    
    for indice , valor in enumerate(lista_tarefas):
        print(f'{indice + 1}) {valor}')

def desfazer():
    if not lista_tarefas:
        system('clear')
        print('nenhuma tarefa para desfazer!!!')
        return
    tarefas_desfeitas.append(lista_tarefas.pop())
    salvar_bd()
    listar()

def refazer():
    if not tarefas_desfeitas:
        system('clear')
        print('nenhuma tarefa para refazer!!!')
        return
    lista_tarefas.append(tarefas_desfeitas.pop())
    salvar_bd()
    listar()

def incluir_tarefa(tarefa):
    if not tarefa.strip():
        system('clear')
        print('voce naão digitou nada!!!')
        return
    lista_tarefas.append(tarefa)
    tarefas_desfeitas.clear()
    salvar_bd()
    listar()

def salvar_bd():
    with open(caminho,'w',encoding='utf8') as bd:
        json.dump(lista_tarefas,bd,ensure_ascii=False , indent=2)  

while True:
    opcao = input(texto).lower()

    # if opcao == 'listar':
    #     listar()

    # elif opcao == 'desfazer':
    #     desfazer()

    # elif opcao == 'refazer':
    #     refazer()

    # else:
    #     incluir_tarefa(opcao)
        

    comandos = {
        'listar': lambda : listar(),
        'desfazer': lambda : desfazer(),
        'refazer': lambda : refazer(),
        'incluir_tarefa': lambda: incluir_tarefa(opcao)
    }

    comando = comandos.get(opcao) if comandos.get(opcao) is not None else comandos['incluir_tarefa']

    comando()