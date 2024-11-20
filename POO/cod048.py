class Cliente:
    def __init__(self, nome) -> None:
        self.nome= nome
        self.endereco= []
    
    def inserir_endereco(self, rua , numero):
        self.endereco.append(Endereco(rua,numero))
    
    def listar(self):
        for endereco in self.endereco:
            print(endereco.rua, endereco.numero , end='\n')

    def __del__ (self):
        print('Deletando', self.nome)

class Endereco:
    def __init__(self,rua , numero) -> None:
        self.rua= rua
        self.numero= numero

    def __del__ (self):
        print('Deletando', self.rua,self.numero)

cli01 = Cliente('lilian')
cli02 = Cliente('jose')

cli01.inserir_endereco('rua001',2)
cli01.inserir_endereco('rua002',22)
cli02.inserir_endereco('rua003',62)
cli02.inserir_endereco('rua004',27)

print(cli01.endereco[0].numero)
cli02.listar()

del cli01

print('###############fim##################')