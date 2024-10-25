
import os

lista_compras= []

while   True:
    opcao= input('Selecione uma opção:\n[N]Novo ,[A]apagar ,[L]listar ,[S]Sair: ').lower()
    os.system('clear')

    if opcao == 's':
        break

    elif opcao == 'n':
        item= input('Digite o novo Item : ')
        lista_compras.append(item)
        

    elif opcao == 'a':
        item = input('Digiet o indice do Item : ')
        try:
            del lista_compras[int(item)]
        except ValueError:
            print('Digite apenas numeros!!!')
        except IndexError:
            print('indice inexistente!!!')

    elif opcao == 'l':
        if len(lista_compras )< 1:
            print('Lista vazia!!!')
        else:
            for i ,a in enumerate(lista_compras):
                print(f'indice = {i} , item = {a}')
        
    else:
        print('Opção invalida!\n Tente novamente.')

