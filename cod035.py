caminho = '/home/uendle/Estudos/Udemy/'
caminho +='arquivo criado com open.txt'

arquivo = open(caminho , 'w')#abre o arquivo
arquivo.close()#fecha o arquivo

with open(caminho , 'a+') as arquivo2:
    #abre o arquivo e fecha atuometicamente com context manager
    arquivo2.write('12345678910\n')#escreve no arquivo
    arquivo2.write('abcdefghijk\n')
    arquivo2.writelines([str(i*2) for i in range(11)])

    arquivo2.seek(0,0)#move o cursor para o inicio
    print(arquivo2.read())

    arquivo2.seek(0,0)#move o cursor para o inicio
    print(arquivo2.readline())

    arquivo2.seek(0,0)#move o cursor para o inicio
    print(arquivo2.readlines())



