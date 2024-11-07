import os
caminho = '/home/uendle/Estudos/Udemy/arquivo criado com open.txt'

with open(caminho,'+a',encoding='utf8') as arquivo:#codificaçao dos caracteres utf8
    arquivo.write('atenção\n')
    arquivo.write('linha2\n')
    arquivo.write('linha3\n')
    arquivo.writelines([str(i) for i in range(10)])

opcao = input('Deseja apagar o arquivo[S|N] ou renomear[R]: ')

if opcao == 's':
    #os.remove(caminho)#remove o arquivo
    os.unlink(caminho)#remove o arquivo
elif opcao == 'r':
    os.rename(caminho,input('Digite o novo nome [.txt]: '))#renomeia e meve o arquivo