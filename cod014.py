import os
import sys

def operacao(opcao):
    if opcao == 'd':
        def duplicar(valor):
            return valor * 2
        return duplicar
    if opcao =='t':
        def triplicar(valor):
            return valor * 3
        return triplicar
    if opcao == 'q':
        def quadruplicar(valor):
            return valor *4
        return quadruplicar
    else:
        print('valor nao encontrado!!')
        sys.exit()

while True:
    
    opcao = input('Digite [d/t/q]: ')

    variavel = operacao(opcao)
    os.system('clear')
    numero = int(input('Digite o numero : '))


    print(variavel(numero))