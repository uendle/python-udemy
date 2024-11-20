class Myopen:
    def __init__(self, caminho,modo) -> None:
        self.caminho= caminho
        self.modo= modo
        self.arquivo = None

    def __enter__(self):
        print('abrindo arquivo!!!')
        self.arquivo = open(self.caminho, self.modo, encoding='utf8')
        return self.arquivo
    def __exit__(self, class_exception_, exception_, treceback_):
        print("fechando")
        self.arquivo.close()

with Myopen('cod058.txt', 'w') as arquivo:
    print('with', arquivo)
    arquivo.write('blablabla\n')
    arquivo.write('blablabla\n')
    arquivo.write('blablabla\n')